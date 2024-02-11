package io.eol.demo.tcpudpserver;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.integration.annotation.ServiceActivator;
import org.springframework.integration.channel.DirectChannel;
import org.springframework.integration.ip.tcp.TcpReceivingChannelAdapter;
import org.springframework.integration.ip.tcp.connection.TcpNetServerConnectionFactory;
import org.springframework.integration.ip.tcp.serializer.ByteArrayCrLfSerializer;
import org.springframework.messaging.MessageChannel;
import org.springframework.messaging.MessageHandler;

@Configuration
public class TcpServerConfig {

    private final int tcpPort = 54321; // Example port

    @Bean
    public TcpNetServerConnectionFactory serverConnectionFactory() {
        TcpNetServerConnectionFactory factory = new TcpNetServerConnectionFactory(tcpPort);
        factory.setSerializer(new ByteArrayCrLfSerializer());
        factory.setDeserializer(new ByteArrayCrLfSerializer());
        return factory;
    }

    @Bean
    public TcpReceivingChannelAdapter inboundAdapter(TcpNetServerConnectionFactory connectionFactory) {
        TcpReceivingChannelAdapter adapter = new TcpReceivingChannelAdapter();
        adapter.setConnectionFactory(connectionFactory);
        adapter.setOutputChannel(inputChannel());
        return adapter;
    }

    @Bean
    public MessageChannel inputChannel() {
        return new DirectChannel();
    }

    @Bean
    @ServiceActivator(inputChannel = "inputChannel")
    public MessageHandler outboundAdapter(TcpNetServerConnectionFactory connectionFactory) {
        return message -> {
            byte[] bytes = (byte[]) message.getPayload();
            System.out.println("Received: " + new String(bytes));
            // Echoing back the received message
            connectionFactory.getConnection().send(message);
        };
    }
}

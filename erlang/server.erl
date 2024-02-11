-module(server).
-export([start/0, tcp_server/0, udp_server/0, accept_loop/1, udp_loop/1, loop/1]).

start() ->
  TcpPid = spawn(?MODULE, tcp_server, []),
  UdpPid = spawn(?MODULE, udp_server, []),
  io:format("TCP server started with PID ~p~n", [TcpPid]),
  io:format("UDP server started with PID ~p~n", [UdpPid]).

tcp_server() ->
  {ok, ListenSocket} = gen_tcp:listen(54321, [binary, {packet, 0}, {reuseaddr, true}, {active, false}]),
  accept_loop(ListenSocket).

accept_loop(ListenSocket) ->
  {ok, Socket} = gen_tcp:accept(ListenSocket),
  spawn(?MODULE, accept_loop, [ListenSocket]), %% Accept next connection
  loop(Socket).

loop(Socket) ->
  case gen_tcp:recv(Socket, 0) of
    {ok, Data} ->
      io:format("TCP received: ~p~n", [Data]),
      gen_tcp:send(Socket, Data), %% Echo back the received data
      loop(Socket); %% Continue the loop to handle more data
    {error, closed} ->
      io:format("TCP connection closed~n"),
      gen_tcp:close(Socket); %% Close the socket when the client disconnects
    Error ->
      io:format("TCP error: ~p~n", [Error]),
      gen_tcp:close(Socket) %% Close the socket on error
  end.

udp_server() ->
  {ok, Socket} = gen_udp:open(12345, [binary]),
  udp_loop(Socket).

udp_loop(Socket) ->
  receive
    {udp, Socket, Host, Port, Data} ->
      io:format("UDP received: ~p from ~p:~p~n", [Data, Host, Port]),
      gen_udp:send(Socket, Host, Port, Data), %% Echo back the data
      udp_loop(Socket) %% Continue the loop to handle more data
  end.

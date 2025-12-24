#!/bin/sh
socat TCP-LISTEN:9001,fork,reuseaddr EXEC:"./chall1" &
socat TCP-LISTEN:9002,fork,reuseaddr EXEC:"./chall2" &
socat TCP-LISTEN:9003,fork,reuseaddr EXEC:"./chall3" &
socat TCP-LISTEN:9004,fork,reuseaddr EXEC:"./chall4" &

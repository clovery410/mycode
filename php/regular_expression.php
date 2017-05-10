<?php
  $input = "TS:201606220452 - 交易所业委会 - 何光红 - 【需求描述】1、为了解决调用B/S子系统的安全问题，要把参数】";
  $pattern = '/^TS:/';
  preg_match($pattern, $input, $matches, PREG_OFFSET_CAPTURE, 3);
  print_r($matches);
 ?>

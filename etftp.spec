%define name etftp
%define version 1.1.3
%define release 15

Summary: The Enhanced Trivial File Transfer Protocol, RFC 1986, client/server
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
License: GPL
Url: https://www.networksorcery.com/enp/protocol/etftp.htm
Group: Networking/File transfer
Buildroot: %{_tmppath}/%{name}-buildroot

%description
ETFTP - Enhanced Trivial File Transfer Protocol. Adaptive transmission
protocol for radio based data transmission.

The idea of ETFTP as a project originated from RFC 1986 in which an
experimental protocol for tactical radio is specified.  On account of
the increasing interest in data transmission over tactical radio, the
code was finally donated to the National Defence Research
Establishment, Dept. of Communication Systems, FOA 72, on condition
that it was released under the terms of the GNU GPL.


Please drop us an e-mail if you do use ``our'' etftp in any research
and/or development...

The code is an extension of W. Richard Stevens implementation of TFTP.
For further reading, study his book "UNIX Network Programming" (ISBN
0-13-949876-1).  See also RFC 998 (NETBLT) and RFC 1350 (TFTP) for more
background and ideas...

For RFC 1986, see, e.g., ftp://nis.nsf.net/documents/rfc/rfc1986.txt.


%prep
 
%setup -q -n etftp-1.1.3

%configure

%build

%make


%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr (-,root,root)
%doc INSTALL TODO USAGE README WhatsNew batchfile.sample
%{_bindir}/*
%{_sbindir}/*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1.3-14mdv2011.0
+ Revision: 618239
- the mass rebuild of 2010.0 packages

* Thu Sep 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1.3-13mdv2010.0
+ Revision: 428629
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-12mdv2009.0
+ Revision: 244950
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.1.3-10mdv2008.1
+ Revision: 136404
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import etftp


* Mon Aug 07 2006 Lenny Cartier <lenny@mandriva.com> 1.1.3-10mdv2007.0
- rebuild

* Wed May 11 2005 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-9mdk
- rebuild

* Mon Feb 23 2004 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-8mdk
- rebuild

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-7mdk
- rebuild

* Thu Aug 29 2002 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-6mdk
- rebuild

* Thu Jul 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-5mdk
- rebuild

* Tue Jan 09 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-4mdk
- rebuild

* Wed Aug 30 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-3mdk
- macros
- BM 

* Wed Apr 26 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.1.3-2mdk
- fix group
- spec helper fixes

* Wed Feb 16 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
 
* Fri Mar 26 1999 Christian Joensson FOA 72 <chj@lin.foa.se>
  [etftp-1.1.3-1]
  - Update to etftp-1.1.3.
    * Fixed bug with integer divisions in timers; lDATAsleep, alarmTimeout.
 
* Fri Aug 28 1998 Christian Joensson FOA 72 <chj@lin.foa.se>
  [etftp-1.1.2-1]
  - Update to etftp-1.1.2.
    * Maximum block size is increased to 1900 bytes data. Non RFC compliant
      in this sense but could increase performance.
    * Maximum baudrate is increased to a maximum of 1000000 (1 Mbps).
 
* Tue Aug 11 1998 Christian Joensson <chj@lin.foa.se>
  [etftp-1.1.1-1]
  - Update to etftp-1.1.1, i.e., fixed symlink to install of etftpd in
    src/Makefile.in
 
Christian Joensson <chj@lin.foa.se>
  [etftp-1.1-1]
  - Update to etftp-1.1.
 
 
* Mon Aug 10 1998 Christian Joensson <chj@lin.foa.se>
  [etftp-1.1-1]
  - Update to etftp-1.1.
 
* Thu May 28 1998 Christian Joensson <chj@lin.foa.se>
  [etftp-1.0-1]
  - First release... 

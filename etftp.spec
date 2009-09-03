%define name etftp
%define version 1.1.3
%define release %mkrel 13

Summary: The Enhanced Trivial File Transfer Protocol, RFC 1986, client/server
Name: %{name}
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
License: GPL
Url: http://www.networksorcery.com/enp/protocol/etftp.htm
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


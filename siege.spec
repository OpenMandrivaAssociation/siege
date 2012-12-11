Summary:	HTTP regression testing and benchmarking utility
Name:		siege
Version:	2.72
Release:	%mkrel 1
License:	GPLv2+
Group:		System/Servers
URL:		http://www.joedog.org/JoeDog/Siege/
Source0:	ftp://ftp.joedog.org/pub/siege/%{name}-%{version}.tar.gz
Patch0:		siege-2.70-makefile.patch
Patch1:		siege-2.72-mdv-format-security.patch
BuildRequires:	openssl-devel

%description
Siege is an HTTP regression testing and benchmarking utility.
It was designed to let web developers measure the performance of their code
under duress, to see how it will stand up to load on the Internet.
Siege supports basic authentication, cookies, HTTP and HTTPS protocols.
It allows the user hit a web server with a configurable number of concurrent
simulated users. Those users place the webserver "under siege."

%prep
%setup -q
%patch0 -p1 -b .good
%patch1 -p1 -b .format

%build
%configure2_5x
%make

%install
%makeinstall_std

install -d %{buildroot}%{_sysconfdir}
install -m0644 doc/urls.txt %{buildroot}%{_sysconfdir}/urls.txt

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING KNOWNBUGS MACHINES NEWS PLATFORM README*
%config(noreplace) %{_sysconfdir}/urls.txt
%config(noreplace) %{_sysconfdir}/siegerc
%{_bindir}/bombardment
%{_bindir}/siege
%{_bindir}/siege.config
%{_bindir}/siege2csv.pl
%{_mandir}/man1/bombardment.1*
%{_mandir}/man1/siege.1*
%{_mandir}/man1/siege.config*
%{_mandir}/man1/siege2csv.1*
%{_mandir}/man5/urls_txt.5*
%{_mandir}/man7/layingsiege.7*


%changelog
* Thu Mar 01 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 2.72-1mdv2011.0
+ Revision: 781643
- new version 2.72

* Sat Aug 21 2010 Funda Wang <fwang@mandriva.org> 2.70-1mdv2011.0
+ Revision: 571584
- update tarball
- New version 2.70

* Mon Apr 12 2010 Funda Wang <fwang@mandriva.org> 2.67-3mdv2010.1
+ Revision: 533650
- rebuild for openssl 1.0

* Sun Sep 20 2009 Thierry Vignaud <tv@mandriva.org> 2.67-2mdv2010.0
+ Revision: 445106
- rebuild

* Fri Jan 23 2009 Jérôme Soyer <saispo@mandriva.org> 2.67-1mdv2009.1
+ Revision: 333012
- New upstream release

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 2.66-4mdv2009.0
+ Revision: 260673
- rebuild
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 2.66-1mdv2008.1
+ Revision: 168232
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 2.66-1mdv2008.0
+ Revision: 79282
- Import siege



* Tue Sep 04 2007 Oden Eriksson <oeriksson@mandriva.com> 2.66-1mdv2008.0
- initial Mandriva package

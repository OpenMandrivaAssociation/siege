Summary:	HTTP regression testing and benchmarking utility
Name:		siege
Version:	3.0.0
Release:	1
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
#% patch0 -p1 -b .good

%build
%configure2_5x
%make

%install
mkdir -p %buildroot/%{_sysconfdir}/siegerc
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

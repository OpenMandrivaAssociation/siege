%define Werror_cflags %nil

Summary:	HTTP regression testing and benchmarking utility
Name:		siege
Version:	2.67
Release:	%mkrel 1
License:	GPL
Group:		System/Servers
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
URL:		http://www.joedog.org/JoeDog/Siege/
Source0:	ftp://ftp.joedog.org/pub/siege/siege-%{version}.tar.gz
Patch0:		siege-2.65-makefile.patch
BuildRequires:	openssl-devel

%description
Siege is an http regression testing and benchmarking utility.
It was designed to let web developers measure the performance of their code
under duress, to see how it will stand up to load on the internet.
Siege supports basic authentication, cookies, HTTP and HTTPS protocols.
It allows the user hit a web server with a configurable number of concurrent
simulated users. Those users place the webserver "under siege."

%prep

%setup -q
%patch0 -p1 -b .good

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d %{buildroot}%{_sysconfdir}
install -m0644 doc/urls.txt %{buildroot}%{_sysconfdir}/urls.txt

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS ChangeLog COPYING KNOWNBUGS MACHINES NEWS PLATFORM README*
%config(noreplace) %{_sysconfdir}/urls.txt
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

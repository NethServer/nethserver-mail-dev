Summary: Development and benchmarking tools for nethserver-mail-common package
Name: nethserver-mail-dev
Version: 1.1.0
Release: 1%{?dist}
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: nethserver-mail-common
BuildRequires: nethserver-devtools

%description
Benchmarking and development configuration for nethserver-mail-common package

%prep
%setup

%build
perl createlinks

%install
rm -rf %{buildroot}
(cd root; find . -depth -print | cpio -dump %{buildroot})
%{genfilelist} %{buildroot} > %{name}-%{version}-filelist

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)
%doc COPYING
%dir %{_nseventsdir}/%{name}-update

%changelog
* Thu Jul 07 2016 Stefano Fancello <stefano.fancello@nethesis.it> - 1.1.0-1
- First NS7 release

* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Use XCLIENT extension only if -addr options is specified.

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Rebuild for automatic package handling. #1870

* Tue Mar 19 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- smtptest: fixed TIME locale for message Date header
- *.spec: use url_prefix macro in URL tag; fixed Release tag expansion; removed Group and BuildRoot tags. Refs #1654 


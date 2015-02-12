Summary: Development and benchmarking tools for nethserver-mail-common package
Name: nethserver-mail-dev
Version: 1.0.3
Release: 1
License: GPL
URL: %{url_prefix}/%{name} 
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch

Requires: nethserver-mail-common

BuildRequires: perl
BuildRequires: nethserver-devtools

%description
Benchmarking and development configuration for nethserver-mail-common package

%prep
%setup

%build
perl createlinks

%install
rm -rf $RPM_BUILD_ROOT
(cd root; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
%{genfilelist} $RPM_BUILD_ROOT > %{name}-%{version}-filelist
echo "%doc COPYING" >> %{name}-%{version}-filelist

%clean
rm -rf $RPM_BUILD_ROOT

%post

%postun

signal_event nethserver-mail-common-save

# Update also amavisd.conf, if nethserver-mail-filter is installed
if rpm --quiet -q nethserver-mail-filter; then
    signal_event nethserver-mail-filter-save
fi

%files -f %{name}-%{version}-filelist
%defattr(-,root,root)

%changelog
* Wed Feb 05 2014 Davide Principi <davide.principi@nethesis.it> - 1.0.3-1.ns6
- Use XCLIENT extension only if -addr options is specified.

* Tue Apr 30 2013 Giacomo Sanchietti <giacomo.sanchietti@nethesis.it> - 1.0.2-1.ns6
- Rebuild for automatic package handling. #1870

* Tue Mar 19 2013 Davide Principi <davide.principi@nethesis.it> - 1.0.1-1.ns6
- smtptest: fixed TIME locale for message Date header
- *.spec: use url_prefix macro in URL tag; fixed Release tag expansion; removed Group and BuildRoot tags. Refs #1654 


# Name of the plugin
%global plugin check_linux_bonding

# No binaries here, do not build a debuginfo package. This is a binary
# package on RHEL/Fedora because it depends on %_libdir which is arch
# dependent
%global debug_package %{nil}

Name:          nagios-plugins-bonding
Version:       1.4
Release:       14%{?dist}
Summary:       Nagios plugin to monitor Linux bonding interfaces

License:       GPLv3+
URL:           http://folk.uio.no/trondham/software/%{plugin}.html
Source0:       http://folk.uio.no/trondham/software/files/%{plugin}-%{version}.tar.gz

# Since we're also building for RHEL5

# Building requires Docbook XML
BuildRequires: libxslt
BuildRequires: libxml2
BuildRequires: docbook-style-xsl
BuildRequires: perl-generators

# Owns the nagios plugins directory
%if 0%{?rhel} > 5 || 0%{?fedora} > 18
Requires: nagios-common
%else
Requires: nagios-plugins
%endif

# Makes the transition to new package name easier for existing
# users of RPM packages
Provides:      check_linux_bonding = %{version}-%{release}
Obsoletes:     check_linux_bonding < 1.3.2

%description
This package contains check_linux_bonding, which is a plugin for
Nagios that checks bonding network interfaces on Linux. The plugin
will report any interfaces that are down (both masters and slaves), as
well as other aspects which may point to a problem with bonded
interfaces.

%prep
%setup -q -n %{plugin}-%{version}

%build
%if 0%{?rhel} > 5 || 0%{?fedora} > 18
pushd man
make clean && make
popd
%else
: # use pre-built man-pages on old systems
%endif

%install
rm -rf %{buildroot}
install -Dp -m 0755 %{plugin} %{buildroot}%{_libdir}/nagios/plugins/%{plugin}
install -Dp -m 0644 man/%{plugin}.8 %{buildroot}%{_mandir}/man8/%{plugin}.8

%files
%doc COPYING CHANGES
%{_libdir}/nagios/plugins/%{plugin}
%{_mandir}/man8/%{plugin}.8*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jul 28 2014 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 1.4-3
- Fix specfile bug that resulted in wrong requires for ownership of
  the nagios plugins directory
- Conditionalize building man pages for rhel6+ and fedora19+ (others
  will use pre-built man pages)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue May 13 2014 Trond Hasle Amundsen <t.h.amundsen@usit.uio.no> - 1.4-1
- Upstream release 1.4

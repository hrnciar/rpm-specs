Name:           libnss-pgsql
Version:        1.5.0
Release:        0.24.beta%{?dist}
Summary:        Name Service Switch library that interface with PostgreSQL

License:        GPL+
URL:            http://pgfoundry.org/projects/sysauth/
Source0:        http://pgfoundry.org/frs/download.php/1878/%{name}-%{version}-beta.tgz
Patch0:         libnss-pgsql-fix_include.patch
Patch1:         libnss-pgsql-1.5.0-beta-exit-in-library.patch

BuildRequires:  gcc
BuildRequires:  libpq-devel, xmlto


%description
Name Service Switch library that interface with PostgreSQL.
See %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}/nss-pgsql.html for the config file.


%prep
%setup -q -n %{name}-%{version}-beta
%patch0 -p1 -b include.rej
%patch1 -p1 -b exit-in-library.rej


%build
%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}
rm -rf ${RPM_BUILD_ROOT}/usr/doc
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'


%ldconfig_scriptlets


%files
%exclude %{_libdir}/*.so
%doc AUTHORS COPYING ChangeLog README doc/nss-pgsql.html doc/caution.png
%{_libdir}/libnss_pgsql.so.2.0.0
%{_libdir}/libnss_pgsql.so.2
%{_libdir}/libnss_pgsql.so


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.24.beta
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.23.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.22.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.21.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.20.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.19.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.18.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.17.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.16.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.15.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.5.0-0.14.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.13.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.12.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.11.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Oct 27 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.5.0-0.10.beta
- Fix reference to docs in %%description when doc dir is unversioned.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.9.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.8.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.7.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.6.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.5.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.4.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-0.3.beta
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 25 2009 Edouard Bourguignon <madko@linuxed.net> - 1.5.0-0.2.beta
- Fix source URL
- Add a patch from M.Tasaka to remove exit() call in the library

* Fri Jan 23 2009 Edouard Bourguignon <madko@linuxed.net> - 1.5.0-0.1.beta
- Upgrade to 1.5.0 beta

* Mon Jan 12 2009 Edouard Bourguignon <madko@linuxed.net> - 1.4.0-2
- Add buildrequires on postgresql-devel

* Thu Jan  3 2008 Edouard Bourguignon <madko@linuxed.net> - 1.4.0-1
- Upgrade to version 1.4.0

* Mon Dec 12 2005 Edouard Bourguignon <madko@linuxed.net> - 1.3-1
- Initial package

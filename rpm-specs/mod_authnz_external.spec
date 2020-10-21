%{!?_httpd_mmn: %global _httpd_mmn %(cat %{_includedir}/httpd/.mmn 2>/dev/null || echo 0-0)}

%global modsuffix authnz_external
%global conffile %{modsuffix}.conf
%global conffile2 10-%{modsuffix}.conf

Summary: An Apache module used for authentication
Name: mod_%{modsuffix}
Version: 3.3.2
Release: 14%{?dist}
License: ASL 1.0
URL: http://code.google.com/p/mod-auth-external/
Source: http://mod-auth-external.googlecode.com/files/%{name}-%{version}.tar.gz
Source1: %{conffile}
Source2: %{conffile2}
Requires: pwauth, httpd-mmn = %{_httpd_mmn}
BuildRequires:  gcc
BuildRequires: httpd-devel

%description
Mod_Auth_External can be used to quickly construct secure, reliable
authentication systems.  It can also be misused to quickly open gaping
holes in your security.  Read the documentation, and use with extreme
caution.


%prep
%setup -q

%build
%{_httpd_apxs} -c -I . %{name}.c


%install
mkdir -p %{buildroot}%{_httpd_moddir} %{buildroot}%{_httpd_confdir} \
         %{buildroot}%{_httpd_modconfdir}
apxs -i -S LIBEXECDIR=%{buildroot}%{_httpd_moddir} -n %{name} %{name}.la
install -p -m 644 -t %{buildroot}%{_httpd_confdir}/ %{SOURCE1}
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
install -p -m 644 -t %{buildroot}%{_httpd_modconfdir}/ %{SOURCE2}
%endif


%files
%{_httpd_moddir}/%{name}.so
%config(noreplace) %lang(en) %{_httpd_confdir}/%{conffile}
%if "%{_httpd_modconfdir}" != "%{_httpd_confdir}"
%config(noreplace) %lang(en) %{_httpd_modconfdir}/%{conffile2}
%endif
%doc AUTHENTICATORS CHANGES README TODO UPGRADE


%changelog
* Fri Aug 28 2020 Joe Orton <jorton@redhat.com> - 3.3.2-14
- use _httpd_apxs, _httpd_mmn macros

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed May 13 2020 Philip Prindeville <philipp@fedoraproject.org> - 3.3.2-12
- Don't duplicate the .d in the configuration directory names.

* Tue May 05 2020 Philip Prindeville <philipp@fedoraproject.org> - 3.3.2-11
- Fix for RHBZ #1426862 and LoadModule early on.

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 3.3.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 Philip Prindeville <philipp@fedoraproject.org> - 3.3.2-1
- Update to latest.

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri May 04 2012 Philip Prindeville <philipp@fedoraproject.org> 3.2.6-1
- Initial version post packaging review.

* Tue Apr 17 2012 Philip Prindeville <philipp@fedoraproject.org> 3.2.6-0
- Initial RPM packaging.

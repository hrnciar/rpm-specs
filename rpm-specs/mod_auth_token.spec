Name:           mod_auth_token
Version:        1.0.5
Release:        22%{?dist}
Summary:        Token based URI access module for Apache

License:        ASL 2.0
URL:            http://code.google.com/p/mod-auth-token/
Source0:        http://mod-auth-token.googlecode.com/files/%{name}-%{version}.tar.gz

Patch0:         mod_auth_token-1.0.5-update-autoconf.patch
Patch1:         mod_auth_token-1.0.5-apply_LDFLAGS.patch
Patch2:         mod_auth_token-1.0.5-fix-Wformat.patch

BuildRequires:  dos2unix
BuildRequires:  httpd-devel
BuildRequires:  libtool

%description
mod_auth_token allows you to generate URIS for a determined
time window, you can also limit them by IP.  This is very
useful to handle file downloads, as generated URIS can't be
hot-linked (after it expires), also it allows you to protect
very large files that can't be piped trough a script languages
due to memory limitation.


%prep
%autosetup -p 1

%{_bindir}/find . -type f -and -not -xtype l -print0 | \
  %{_bindir}/xargs -0 %{_bindir}/dos2unix -k

%{_bindir}/autoreconf -fiv


%build
%configure
%make_build


%install
# %%make_install doesn't work here.
%{__install} -d %{buildroot}%{_libdir}/httpd/modules
%{__install} -pm 755 .libs/%{name}.so %{buildroot}%{_libdir}/httpd/modules


%files
%doc ChangeLog README
%license AUTHORS LICENSE
%{_libdir}/httpd/modules/%{name}.so


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-22
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Feb 12 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.5-18
- Update patch0 to fix Automake parameters
- Fix end-of-line-encoding for several files
- Drop empty NEWS file
- Fix description

* Tue Feb 12 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.5-17
- Add patch to fix -Wformat

* Thu Feb 07 2019 Björn Esser <besser82@fedoraproject.org> - 1.0.5-16
- Update spec file to match recent guidelines
- Add patch to update deprecated autoconf macros
- Add patch to apply LDFLAGS properly

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue May 29 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 1.0.5-2
- Apply package review patch from Lukáš Zapletal.

* Thu May 24 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 1.0.5-1
- Don't use full path for apxs, since it's moved around in later fedoras.

* Thu May 24 2012 Jan-Frode Myklebust <janfrode@tanso.net> - 1.0.5
- Initial build.

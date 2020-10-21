%global __python    %{__python3}

%global commit      ae3eff1063a6fc75cf1a99d72470c58ca0333f3e
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global gitdate     20140518

Name:           system-config-repo
Version:        0
Release:        27.%{gitdate}git%{shortcommit}%{?dist}
Summary:        Administrate a single yum repository file

License:        MIT
URL:            https://github.com/leamas/system-config-repo
Source0:        %{url}/archive/%{commit}/%{name}-0-%{shortcommit}.tar.gz
                # Created by tools/make_rpm, left in dist directory.
Source1:        version
BuildArch:      noarch

Buildrequires:  python3-devel
BuildRequires:  desktop-file-utils
Requires:       gtk3
Requires:       hicolor-icon-theme
Requires:       python(abi) = %{python3_version}
Requires:       python3-gobject
Requires:       redhat-lsb-core
Requires:       sudo


%description
system-config-repo provides a graphical interface to a single yum repository
file in /etc/yum.repos.d. Using the GUI user can inspect and modify whether
the repository is enabled and/or signed. It's also possible to see the
underlying file.

Application is primarily intended as a GUI for packaged 3rd-party
repositories but is designed to work in a consistent way for any
repository file.


%prep
%setup -qn %{name}-%{commit}
cp %{SOURCE1} version


%build


%install
make DESTDIR=%{buildroot} install
desktop-file-validate \
    %{buildroot}%{_datadir}/applications/system-config-repo.desktop
%py_byte_compile %{__python3} %{buildroot}%{_datadir}/%{name}/scripts/

%files
%doc README.md LICENSE
%{_bindir}/system-config-repo
%{_datadir}/system-config-repo
%{_datadir}/icons/hicolor/*/apps/scr-repo.png
%{_datadir}/icons/hicolor/*/mimetypes/application-x-yum-repositories.png
%{_datadir}/mime/packages/x-yum-repositories.xml
%{_datadir}/applications/system-config-repo.desktop
%{_mandir}/man1/system-config-repo*
%attr(440,-,-) %config(noreplace) /etc/sudoers.d/system-config-repo


%changelog
* Mon Sep 07 2020 Than Ngo <than@redhat.com> - 0-27.20140518gitae3eff1
- Fix FTBFS

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-26.20140518gitae3eff1
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-25.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0-24.20140518gitae3eff1
- Rebuilt for Python 3.9

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0-23.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 0-22.20140518gitae3eff1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0-21.20140518gitae3eff1
- Rebuilt for Python 3.8

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-20.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-19.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-18.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0-17.20140518gitae3eff1
- Rebuilt for Python 3.7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-16.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jan 18 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0-15.20140518gitae3eff1
- Remove obsolete scriptlets

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-14.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-13.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0-12.20140518gitae3eff1
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-11.20140518gitae3eff1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-10.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-9.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-8.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Sep 27 2014 Rex Dieter <rdieter@fedoraproject.org> 0-7.20140518gitae3eff1
- update/optimize mimeinfo scriplets

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-6.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 28 2014 Kalev Lember <kalevlember@gmail.com> - 0-5.20140518gitae3eff1
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Sun May 18 2014 Alec Leamas <leamas.alec@gmail.com> - 0-4.20140518gitae3eff1
- Fix icon bug, upstream updates.

* Sat Jan 25 2014 Alec Leamas <leamas.alec@gmail.com> - 0-2.20140117git3318cd6
- Adding missing R: redhat-lsb-core (bz #1057824).

* Mon Jan 20 2014 Alec Leamas <leamas.alec@gmail.com> - 1.20140117git3318cd6
- Initial release.

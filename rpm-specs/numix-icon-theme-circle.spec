%global commit cc59306034aa4f558a5c5015fc801e8d0149532e
%global gittag 19.12.27

%global gitdate %(date -d %(echo %{gittag} | tr -d '.') +%Y%m%d)
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		numix-icon-theme-circle
Version:	0.1.0
Release:	27.%{gitdate}.git%{shortcommit}%{?dist}
Summary:	Numix Project circle icon theme

Source:		https://github.com/numixproject/numix-icon-theme-circle/archive/%{commit}/%{name}-%{commit}.tar.gz

License:	GPLv3
URL:		https://github.com/numixproject/numix-icon-theme-circle

BuildArch:	noarch
Requires:	filesystem
Requires:	numix-icon-theme

%description
Numix is the official icon theme from the Numix project.
It is heavily inspired by, and based upon parts of the Elementary,
Humanity and Gnome icon themes.

%prep
%autosetup -n %{name}-%{commit}

%build
find -type f -executable -exec chmod -x {} \;

%install
install -d %{buildroot}%{_datadir}/icons

mkdir -p %{buildroot}%{_datadir}/doc/%{name}
cp -pr Numix-Circle %{buildroot}%{_datadir}/icons/Numix-Circle
cp -pr Numix-Circle-Light %{buildroot}%{_datadir}/icons/Numix-Circle-Light

%post
/bin/touch --no-create %{_datadir}/icons/Numix-Circle &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/Numix-Circle-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Numix-Circle &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/Numix-Circle-Light &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle-Light &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Circle-Light &>/dev/null || :

%files
%license LICENSE
%doc README.md
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-27.20191227.gitcc59306
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jan 16 2020 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-26.20191227.gitcc59306
- Update to release 19.12.27

* Tue Nov 12 2019 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-25.20191106.git4ccd81e
- Update to release 19.11.06

* Fri Sep 27 2019 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-24.20190920.git74295b4
- Update to release 19.09.20

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23.20190415.gitb30426e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Apr 18 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-22.20190415.gitb30426e
- Update to release 19.04.15

* Sun Feb 24 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-21.20190222.gita673d9d
- Update to release 19.02.22

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20.20190124.gitda33f8b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jan 27 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-19.20190124.gitda33f8b
- Update to release 19.01.24

* Fri Jan 18 2019 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-18.20181201.git085899f
- Update to release 18.12.01

* Tue Oct 09 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-17.20181003.git7637f41
- Update to release 18.10.03
- Bring more in line with packaging guidelines

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16.git5a11140
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-15.git5a11140
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14.git5a11140
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 0.1.0-13.git5a11140
- rebuilt

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-12.gitc3aefdb
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-11.gitc3aefdb
- rebuilt

* Tue Jun 14 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-10.git475d649
- rebuilt

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-9.git475d649
- Requires filesystem

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-8.git475d649
- Fix file permissions

* Tue May 03 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-9.git475d649
- spec file fixes

* Wed Apr 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-8.git475d649
- license tag for license file, diffable lines

* Tue Apr 19 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-7.git475d649
- split spec file

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-6.git475d649
- adjust groups and tabstops

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-5.git475d649
- fix sources setup and relative dirs

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-4.git475d649
- add license and readme files

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-3.git475d649
- require gdk-pixbuf2

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-2.git475d649
- refactor for git use

* Sun Jan 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-1.git475d649
- Refactor to build real srpms
- Repackaging
- Adding Shine and uTouch


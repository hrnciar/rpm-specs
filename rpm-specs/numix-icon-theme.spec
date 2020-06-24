%global commit ea068b43aba040ece617eb9dcc7ca16bfbabf816
%global gittag 20.03.20

%global gitdate %(date -d %(echo %{gittag} | tr -d '.') +%Y%m%d)
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:		numix-icon-theme
Version:	0.1.0
Release:	24.%{gitdate}.git%{shortcommit}%{?dist}
Summary:	Numix Project icon theme

Source:		https://github.com/numixproject/numix-icon-theme/archive/%{commit}/%{name}-%{commit}.tar.gz

License:	GPLv3
URL:		https://github.com/numixproject/numix-icon-theme

BuildArch:	noarch
Requires:	filesystem
Requires:	gnome-icon-theme
Requires:	hicolor-icon-theme

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
cp -pr Numix %{buildroot}%{_datadir}/icons/Numix
cp -pr Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light

%post
/bin/touch --no-create %{_datadir}/icons/Numix &>/dev/null || :
/bin/touch --no-create %{_datadir}/icons/Numix-Light &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/Numix &>/dev/null
    /bin/touch --no-create %{_datadir}/icons/Numix-Light &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix &>/dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Light &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix &>/dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/Numix-Light &>/dev/null || :

%files
%license license
%doc readme.md
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light

%changelog
* Sat Mar 21 2020 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-24.20200320.gitea068b4
- Update to release 20.03.20

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-23.20190920.gitcfef86f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 27 2019 Brendan Early <mymindstorm@evermiss.net> - 0.1.0-22.20190920.gitcfef86f
- Update to release 19.09.20

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-21.20180717.git763489f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-20.20180717.git763489f
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 09 2018 Brendan Early <mymindstorm1@gmail.com> - 0.1.0-19.20180717.git763489f
- Update to release 18.07.17
- Bring more in line with packaging guidelines

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-18.git271471c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 08 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-17.git271471c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-16.git271471c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Apr 18 2017 Fedora <sspreitz@redhat.com> - 0.1.0-15.git271471c
- rebuilt

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-14.git294ec8e
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-13.git294ec8e
- rebuilt

* Tue Jun 14 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-12.git101307f
- rebuilt

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-11.git101307f
- Requires filesystem

* Mon Jun 13 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-10.git101307f
- Fix file permissions

* Tue May 03 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-9.git101307f
- spec file fixes

* Wed Apr 20 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-8.git101307f
- license tag for license file, diffable lines

* Tue Apr 19 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-7.git101307f
- split spec file

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-6.git101307f
- adjust groups and tabstops

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-5.git101307f
- fix sources setup and relative dirs

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-4.git101307f
- add license and readme files

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-3.git101307f
- require gdk-pixbuf2

* Sat Apr 16 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-2.git101307f
- refactor for git use

* Sun Jan 24 2016 Sascha Spreitzer <sspreitz@redhat.com> - 0.1.0-1.git101307f
- Refactor to build real srpms
- Repackaging
- Adding Shine and uTouch

%global majorver 1.0
%global appdata_name org.xubuntu.XfpanelSwitch

Name:		xfpanel-switch
Version:	1.0.7
Release:	7%{?dist}
Summary:	A simple application to manage Xfce panel layouts

License:	GPLv3
URL:		https://launchpad.net/%{name}
Source0:	https://launchpad.net/%{name}/%{majorver}/%{version}/+download/%{name}-%{version}.tar.bz2

%if 0%{?fedora}
BuildRequires:	python3-devel
%endif

BuildRequires:	gettext
BuildRequires:	intltool
BuildRequires:	libappstream-glib
BuildRequires:	desktop-file-utils
BuildArch:	noarch
Requires:	xfce4-panel

%description
A simple application to manage Xfce panel layouts

With the modular Xfce Panel, a multitude of panel layouts can be created. 
This tool makes it possible to backup, restore, import, and export these 
panel layouts.

%prep
%setup -q

%build
#cannot use configure macro here
./configure --prefix=/usr
%make_build

%install
%make_install

rm -f %{buildroot}%{_docdir}/%{name}/COPYING

%find_lang %{name}

%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{appdata_name}.appdata.xml

%files -f %{name}.lang
%license COPYING
%doc NEWS AUTHORS README INSTALL
%{_datadir}/%{name}/*
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/metainfo/*.appdata.xml

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.7-2
- Rebuilt for Python 3.7

* Tue Apr 17 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.7-1
- Update to 1.0.7

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.6-3
- Truly fix files and appdata issues

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.6-2
- Fix build problems

* Wed Mar 28 2018 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.6-1
- Update to 1.0.6
- Change appdata filename
- Drop upstreamed patches
- Stop removing xubuntu layout

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Apr 15 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.4-2
- Added fedora and el conditionals

* Thu Apr 14 2016 Mukundan Ragavan <nonamedotc@fedoraproject.org> - 1.0.4-1
- Updated to v1.0.4

* Mon Mar 07 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-3
- Added italian translation

* Sun Mar 06 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-2
- Add desktop-file-validate for .desktop files
- Fix buildrequires
- Add appdata file and corresponding BR

* Sat Mar 05 2016 Mukundan Ragavan <nonamedotc@gmail.com> - 1.0.3-1
- Inital package 

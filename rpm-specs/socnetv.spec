%global debug_package %{nil}

Name:		socnetv
Version:	2.5
Release:	2%{?dist}
License:	GPLv3
Summary:	A Social Networks Analyser and Visualiser
URL:		https://socnetv.org/
Source0:	https://github.com/socnetv/app/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/socnetv/app/issues/106
Patch0:		%{name}-%{version}.patch
# https://github.com/socnetv/app/issues/105
Patch1:		%{name}_i18n.patch
BuildRequires:	gcc-c++
BuildRequires:	gzip
BuildRequires:	qt5-linguist
BuildRequires:	desktop-file-utils
# qt5-qtbase-devel
BuildRequires:	pkgconfig(Qt5)
# qt5-qtsvg-devel
BuildRequires:	pkgconfig(Qt5Svg)
# qt5-qtcharts-devel
BuildRequires:	pkgconfig(Qt5Charts)

%description
Social Network Visualizer (SocNetV) is a cross-platform, user-friendly
free software application for social network analysis and visualization.


%prep
%autosetup -p 0 -n app-%{version}
gunzip changelog.gz
chmod -x changelog

%build
lrelease-qt5 socnetv.pro
qmake-qt5
%{make_build}


%install
%{make_install} INSTALL_ROOT=%{buildroot}


%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop


%post
/usr/bin/update-desktop-database &> /dev/null || :


%postun
/usr/bin/update-desktop-database &> /dev/null || :


%files
%license COPYING
%doc AUTHORS changelog NEWS README.md
%{_bindir}/%{name}
%{_datadir}/%{name}/%{name}_*.qm
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/metainfo/%{name}.appdata.xml
%{_mandir}/man1/%{name}.1.gz


%changelog
* Tue Jun 16 2020 TI_Eugene <ti.eugene@gmail.com> 2.5-2
- Spec file fixes

* Tue Jun 09 2020 TI_Eugene <ti.eugene@gmail.com> 2.5-1
- Initital build

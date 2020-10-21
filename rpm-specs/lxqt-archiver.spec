%global __provides_exclude_from %{_libexecdir}/lxqt-archiver/*$

Name:    lxqt-archiver
Summary: A simple & lightweight desktop-agnostic Qt file archiver
Version: 0.2.0
Release: 1%{?dist}
License: GPLv2+
URL:     https://lxqt.github.io/
Source0: https://github.com/lxqt/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Source1: %{name}.appdata.xml
BuildRequires: %{?fedora:cmake}%{!?fedora:cmake3} >= 3.0
BuildRequires: pkgconfig(lxqt) >= 0.13.0
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: qt5-linguist
BuildRequires: desktop-file-utils
BuildRequires: lxqt-build-tools
BuildRequires: libfm-qt-devel
BuildRequires: json-glib-devel
BuildRequires: libexif-devel
BuildRequires: libappstream-glib
# Fix compilation error with hardened security flags
Patch0: https://github.com/lxqt/lxqt-archiver/commit/ecec793534c841cce935093d1e08b9aa227565a8.patch
# Fix comparison of integer expressions of different signedness: ‘size_t’
Patch1: https://github.com/lxqt/lxqt-archiver/commit/b968e339bebe80ddd017ddf16f70bee52261e533.patch

%if 0%{?el7}
BuildRequires:  devtoolset-7-gcc-c++
%else
BuildRequires:  gcc-c++
%endif

%description
%{summary}.

%package l10n
BuildArch:      noarch
Summary:        Translations for lxqt-archiver
Requires:       lxqt-archiver
%description l10n
This package provides translations for the lxqt-archiver package.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%if 0%{?el7}
scl enable devtoolset-7 - <<\EOF
%endif
mkdir -p %{_target_platform}
pushd %{_target_platform}
   %{cmake_lxqt} -DUSE_QT5=TRUE -DPULL_TRANSLATIONS=NO ..
popd

make %{?_smp_mflags} -C %{_target_platform}

%if 0%{?el7}
EOF
%endif

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

desktop-file-edit \
    --remove-category=LXQt --add-category=X-LXQt \
    %{buildroot}%{_datadir}/applications/%{name}.desktop
mkdir -p %{buildroot}%{_datadir}/lxqt/translations/%{name}
mkdir -p %{buildroot}%{_metainfodir}/
cp %{SOURCE1} %{buildroot}%{_metainfodir}/
appstream-util validate-relax --nonet %{buildroot}%{_metainfodir}/*.appdata.xml

%find_lang %{name} --with-qt

%files 
%doc CHANGELOG AUTHORS README.md
%license LICENSE
%{_bindir}/%{name}
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/isoinfo.sh
%{_libexecdir}/%{name}/rpm2cpio
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_metainfodir}/%{name}.appdata.xml
%dir %{_datadir}/%{name}


%files l10n -f %{name}.lang
%doc CHANGELOG AUTHORS README.md
%license LICENSE
%dir %{_datadir}/%{name}/translations
%{_datadir}/%{name}/translations/%{name}_arn.qm
%{_datadir}/%{name}/translations/%{name}_ast.qm

%changelog
* Wed Aug 26 2020 Zamir SUN <sztsian@gmail.com> - 0.2.0-1
- Initial lxqt-archiver 0.2.0

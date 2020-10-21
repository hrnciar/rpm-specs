Name:           qt-avif-image-plugin
Version:        0.3.1
Release:        1%{?dist}
Summary:        Qt plug-in to read/write AVIF images

License:        BSD
URL:            https://github.com/novomesk/qt-avif-image-plugin
Source0:        %url/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc
BuildRequires:  pkgconfig(libavif)
BuildRequires:  pkgconfig(Qt5)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  qt5-rpm-macros
Requires:       kf5-filesystem
Requires:       shared-mime-info

%description
Qt plug-in to allow Qt and KDE based applications to read/write AVIF images.

%prep
%autosetup

%build
%cmake
%cmake_build

%install
%cmake_install

# Install MIME type
mkdir -p %{buildroot}%{_datadir}/mime/packages/
cp -aR share/mime/packages/*.xml %{buildroot}%{_datadir}/mime/packages/.

%post
# First install
if [ $1 -eq 1 ]; then
    sed -i 's@\(MimeType=.*\)@\1image/avif;image/avif-sequence;@' %{_datadir}/kservices5/imagethumbnail.desktop
fi

%postun
# Uninstall
if [ $1 -eq 0 ]; then
    sed -i 's@image/avif;image/avif-sequence;@@' %{_datadir}/kservices5/imagethumbnail.desktop
fi

# We detect if the user has updated imagethumbnail.desktop (via kio-extras)
# and reapply our patch
%transfiletriggerin -- %{_datadir}/kservices5/
grep -w imagethumbnail.desktop | xargs grep -q "avif" || sed -i 's@\(MimeType=.*\)@\1image/avif;image/avif-sequence;@' %{_datadir}/kservices5/imagethumbnail.desktop

%files
%license LICENSE PATENTS.txt
%doc README.md
%{_qt5_plugindir}/imageformats/libqavif.so
%{_datadir}/kservices5/qimageioplugins/avif.desktop
%{_datadir}/kservices5/qimageioplugins/avifs.desktop
%{_datadir}/mime/packages/*.xml

%changelog
* Sun Aug 23 15:43:15 CEST 2020 Robert-André Mauchin <zebob.m@gmail.com> - 0.3.1-1
- Initial RPM

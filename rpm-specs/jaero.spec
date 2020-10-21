Name:           jaero
Version:        1.0.4.11
Release:        4%{?dist}
Summary:        A SatCom ACARS demodulator and decoder for the Aero standard

# LGPLv2+ for JAERO/gui_classes/console.cpp
License:        MIT and LGPLv2+
URL:            http://jontio.zapto.org/hda1/jaero.html
Source0:        https://github.com/jontio/JAERO/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.xz
Source1:        %{name}.appdata.xml
# Fix for Werror=format-security
Patch0:         bcb5b78c74f06cc878cb347b9f99b08cddfafef4.patch
# Fix support system qcustomplot
Patch1:         fe604fb7e221fc615c0526a48f1f73954d6e70bb.patch

BuildRequires:  gcc-c++
BuildRequires:  libcorrect-devel
BuildRequires:  pkgconfig
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5PrintSupport)
BuildRequires:  pkgconfig(Qt5Sql)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(libacars)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  kiss-fft-static
BuildRequires:  qcustomplot-qt5-devel
BuildRequires:  libappstream-glib

Requires:       hicolor-icon-theme
Requires:       unzip%{?_isa}

%description
JAERO is a program that demodulates and decodes Classic Aero ACARS (Aircraft
Communications Addressing and Reporting System) messages sent from satellites to
aeroplanes (SatCom ACARS), commonly used when planes are beyond VHF range.

Demodulation is performed using the soundcard.

Such signals are typically around 1.5Ghz and can be received with a
low-gain antenna that can be home-brewed in conjunction with an
RTL-SDR dongle.

%prep
%autosetup -p1 -n JAERO-%{version}
## remove bundled libs
# rm -rf kiss_fft130
rm -rf kiss_fft130/kiss_fft*
rm -rf libacars-*
rm -rf libcorrect
rm -rf libogg-*
rm -rf libvorbis-*
rm -rf qcustomplot

# Unbundle kiss-fft
%global TYPE double
echo "INCLUDEPATH += %{_includedir}/kissfft" >> JAERO/JAERO.pro
echo "LIBS += -lkiss_fft_%{TYPE} -lkiss_fftnd_%{TYPE} -lkiss_fftndr_%{TYPE} -lkiss_fftr_%{TYPE} -lkiss_kfc_%{TYPE}" >> JAERO/JAERO.pro
sed -i 's|../kiss_fft130/kiss_fft|kiss_fft|' JAERO/fftwrapper.h
sed -i 's|../kiss_fft130/kiss_fft|kiss_fft|' JAERO/fftrwrapper.h
sed -i 's|../kiss_fft130/kiss_fft|kiss_fft|' JAERO/DSP.h

# Unbundle libacars
# Use prope qcustomplot Qt5 lib
sed -e '/QMAKE_CXXFLAGS_RELEASE/d' \
    -e '/VORBIS_PATH/d' \
    -e '/OGG_PATH/d' \
    -e '/LIBACARS_PATH/d' \
    -e 's|lqcustomplot|lqcustomplot-qt5|' \
    -e '/kiss_fft130\/kiss_fft/d' -i JAERO/JAERO.pro

# Unbundle libcorrect
sed -i 's|../libcorrect/include/||' JAERO/jconvolutionalcodec.h

# Correct desktop-file
mv JAERO/JAERO.desktop JAERO/%{name}.desktop
sed -e "s|/opt/jaero/JAERO|%{_bindir}/%{name}|" \
    -e "s|/opt/jaero/jaero.ico|%{name}|" -i JAERO/%{name}.desktop

%build
mkdir JAERO/build
pushd JAERO/build
    %{qmake_qt5} ..
    %make_build
popd

%install
install -Dpm 0755 JAERO/build/JAERO  %{buildroot}%{_bindir}/%{name}
install -Dpm 0644 JAERO/images/primary-modem.svg %{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
desktop-file-install JAERO/%{name}.desktop
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%check
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/%{name}.appdata.xml

%files
%license JAERO/LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/metainfo/%{name}.appdata.xml

%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4.11-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4.11-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 31 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.4.11-2
- Small spec improvments

* Thu Oct 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 1.0.4.11-1
- Initial release for Fedora

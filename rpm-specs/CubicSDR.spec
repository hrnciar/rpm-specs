%global commit d2f93335236ef37557057d7b71c46969bec14471
%global shortcommit %(c=%{commit}; echo ${c:0:7})
%global snapshotdate 20200226
Name:           CubicSDR
Version:        0.2.5
Release:        4.%{snapshotdate}git%{shortcommit}%{?dist}
Summary:        Cross-Platform Software-Defined Radio Panadapter

# The primary license of CubicSDR is GPLv2+.
# There are multiple third party libraries bundled in the source of CubicSDR.
# external/loadpng/ and external/tinyxml/ use the zlib/libpng license
# external/rs232/, external/liquid-dsp/, src/util/DataTree* use the MIT/X11 (BSD like) license
# Note: external/hamlib/ and external/rtaudio/ are provided by the source, but at
#  build and run time we use system-provided copies of these libraries
License:        GPLv2+ and MIT and zlib
URL:            https://cubicsdr.com
Source0:        https://github.com/cjcliffe/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Source1:        CubicSDR
Patch0:         gdk-backend-desktop.patch
# Upstream includes local copies of librs232 and tinyxml unfortunately.
#    https://github.com/cjcliffe/CubicSDR/issues/670
Provides: bundled(librs232) = 0.21
Provides: bundled(tinyxml) = 2.6.2
# Upstream includes local copy of lodepng not present in Fedora already
Provides: bundled(lodepng) = 20180809
BuildRequires:  cmake gcc-c++ desktop-file-utils
# Library dependencies
BuildRequires: SoapySDR-devel
BuildRequires: wxGTK-devel
BuildRequires: hamlib-devel
BuildRequires: fftw-devel
BuildRequires: rtaudio-devel
BuildRequires: liquid-dsp-devel >= 1.3.2

%description
CubicSDR is a cross-platform Software-Defined Radio application which
allows you to navigate the radio spectrum and demodulate any signals
you might discover.  It currently includes several common analog
demodulation schemes such as AM and FM and will support digital modes
in the future.


%prep
%autosetup -n %{name}-%{commit} -p1


%build
%cmake -Wno-dev -DCMAKE_BUILD_TYPE=Release -DUSE_HAMLIB=1 -DUSE_SYSTEM_RTAUDIO=1 .
%make_build


%install
%make_install
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop
# Move executable to libexecdir, leave CLI start script in bindir
mkdir -p %{buildroot}/%{_libexecdir}/%{name}
mv %{buildroot}/%{_bindir}/CubicSDR %{buildroot}/%{_libexecdir}/%{name}/%{name}
install -m 0755 %{SOURCE1} %{buildroot}/%{_bindir}/%{name}


%files
%license LICENSE
%{_libexecdir}/*
%{_bindir}/*
# Upstream includes local copies of Bitstream Vera fonts
#    https://github.com/cjcliffe/CubicSDR/issues/669
%{_datadir}/cubicsdr/
%{_datadir}/applications/%{name}.desktop


%changelog
* Mon Apr 20 2020 Matt Domsch <matt@domsch.com> 0.2.5-4.20200407gitd2f9333
- rebuild for hamlib-devel 4.0.0

* Thu Apr  9 2020 Matt Domsch <matt@domsch.com> 0.2.5-3.20200407gitd2f9333
- move executable to libexecdir
- delete unused external libraries source tarball
- address review comments, spec file cleanups

* Wed Apr  8 2020 Matt Domsch <matt@domsch.com> 0.2.5-2.20200407gitd2f9333
- move env GDK_BACKEND=x11 into the desktop start file

* Tue Apr  7 2020 Matt Domsch <matt@domsch.com> 0.2.5-1.20200407gitd2f9333
- Latest upstream plus newer liquid-dsp library

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-4.20180806gita7e4d91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-3.20180806gita7e4d91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.4-2.20180806gita7e4d91
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Aug  7 2018 Matt Domsch <matt@domsch.com> 0.2.4-1.20180806gita7e4d91
- Initial Fedora packaging

Name:           dsp
Version:        1.6
Release:        3%{?dist}
Summary:        An audio processing program with an interactive mode

# Everything is ISC, except for g2reverb, which is GPLv2+, and reverb, which is LGPLv2+
License:        ISC and GPLv2+ and LGPLv2+
URL:            https://github.com/bmc0/dsp
Source0:        https://github.com/bmc0/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# https://github.com/bmc0/dsp/commit/8581fb454ba5ffd9386e07898c6f4cb77969b6ed
Patch0:         dsp-1.6-zita-convolver-4.patch

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  fftw-devel
BuildRequires:  ladspa-devel
BuildRequires:  libao-devel
BuildRequires:  libmad-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool-ltdl-devel
BuildRequires:  pulseaudio-libs-devel
BuildRequires:  zita-convolver-devel


%description
dsp is an audio processing program with an interactive mode.


%package -n ladspa-dsp-plugin
Summary:        dsp's LADSPA frontend

Requires:       ladspa


%description -n ladspa-dsp-plugin
dsp's LADSPA frontend.


%prep
%autosetup -p1


%build
./configure --libdir=/%{_lib} --disable-ffmpeg

export CFLAGS="%{optflags}"
export CXXFLAGS="%{optflags}"
%make_build


%install
%make_install


%files
%license LICENSE LICENSE.GPL2 LICENSE.LGPL2_1
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*


%files -n ladspa-dsp-plugin
%license LICENSE LICENSE.GPL2 LICENSE.LGPL2_1
%doc README.md
%{_libdir}/ladspa/ladspa_dsp.so


%changelog
* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Apr 09 2020 Nikola Forró <nforro@redhat.com> - 1.6-2
- Fix typo in gcc-c++ build dependency

* Thu Feb 27 2020 Nikola Forró <nforro@redhat.com> - 1.6-1
- Initial package

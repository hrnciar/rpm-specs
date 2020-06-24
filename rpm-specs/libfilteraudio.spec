Name:       libfilteraudio
Version:    0.0.1
Release:    8%{?dist}
Summary:    Lightweight audio filtering library made from webrtc code

License:    BSD
URL:        https://github.com/irungentoo/filter_audio/
Source0:    %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  cmake
BuildRequires:  pkgconfig(portaudio-2.0)
BuildRequires:  pkgconfig(sndfile)


%description
Lightweight audio filtering library made from webrtc code.


%package devel
Summary:        Development files for libfilteraudio
Requires:       %{name}%{?_isa} = %{version}-%{release}


%description devel
Development files for libfilteraudio, the lightweight audio 
filtering library made from webrtc code.


%prep
%autosetup -n filter_audio-%{version}


%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{__global_ldflags}"
%make_build


%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_lib}
find %{buildroot} -name '*.a' -delete


%files
%doc README
%{_libdir}/libfilteraudio.so.*


%files devel
%{_includedir}/filter_audio.h
%{_libdir}/libfilteraudio.so
%{_libdir}/pkgconfig/filteraudio.pc


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-4
- Remove ldconfig

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 31 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-2
- Clean-up the SPEC

* Sat Jul 29 2017 Robert-André Mauchin <zebob.m@gmail.com> - 0.0.1-1
- First RPM release


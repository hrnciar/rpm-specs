Name:		streameye
Version:	0.9
Release:	4%{?dist}
Summary:	Simple MJPEG streamer for Linux
License:	GPLv3
URL:		https://github.com/ccrisan/streameye
Source0:	https://github.com/ccrisan/streameye/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
%description
Simple MJPEG streamer for Linux. It acts as an HTTP server and is capable
of serving multiple simultaneous clients.

It will feed the JPEGs read at input to all connected clients, in a MJPEG
stream. The JPEG frames at input may be delimited by a given separator.
In the absence of a separator, streamEye will auto-detect all JPEG frames.

%prep
%setup -qn %{name}-%{version}

%build
%make_build CFLAGS='%{optflags} -pthread -D_GNU_SOURCE' BINDIR=%{_bindir}

%install
mkdir -p %{buildroot}%{_bindir}
cp -p %{name} %{buildroot}%{_bindir}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Jan Kalina <honza889@gmail.com> - 0.9-1
- Upgraded streameye version

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Aug 22 2017 Jan Kalina <jkalina@redhat.com> - 0.8-3
- Preserve timestamps on copy, macros fix

* Fri Jun 2 2017 Jan Kalina <jkalina@redhat.com> - 0.8-2
- Correct using macros in spec

* Wed Apr 26 2017 Jan Kalina <jkalina@redhat.com> - 0.8-1
- Initial Packaging

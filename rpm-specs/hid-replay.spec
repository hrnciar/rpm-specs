Name:           hid-replay
Version:        0.7.1
Release:        11%{?dist}
Summary:        HID Input device recorder and replay

License:        GPLv2+
URL:            https://github.com/bentiss/%{name}
Source0:        https://github.com/bentiss/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

Patch01:       0001-force-hid-replay-build-for-RHEL-6.patch

BuildRequires:  automake gcc
BuildRequires:  asciidoc xmlto

%description
%{name} is a tool that allow users to capture hidraw description and
events in order to replay them through the uhid kernel module.

%prep
%setup -q
%patch01 -p1

%build
autoreconf -v --install || exit 1
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%license COPYING
%doc README
%{_bindir}/hid-replay
%{_bindir}/hid-recorder
%{_mandir}/man1/hid-replay.1*
%{_mandir}/man1/hid-recorder.1*

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Feb 19 2018 Peter Hutterer <peter.hutterer@redhat.com> 0.7.1-7
- Add BR for gcc

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.7.1-2
- Bump for rebuilds of f26 and f25

* Fri Feb 19 2016 Benjamin Tissoires <benjamin.tissoires@redhat.com> 0.7.1-1
- Initial package

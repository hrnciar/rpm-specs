Name:           psi-notify
Version:        1.2.1
Release:        2%{?dist}
Summary:        Alert when your machine is becoming over-saturated

License:        MIT
URL:            https://github.com/cdown/psi-notify
Source0:        %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsystemd)
# Fedora 31's unit presets defaults to enabling, avoid it
%if 0%{?fedora} >= 32
BuildRequires:  systemd-rpm-macros
%endif

%description
psi-notify is a minimal unprivileged notifier for system-wide resource pressure
using PSI.

This can help you to identify misbehaving applications on your machine before
they start to severely impact system responsiveness, in a way which MemAvailable
or other metrics cannot.


%prep
%autosetup


%build
export CC=gcc
%set_build_flags
%make_build


%install
install -Dp %{name} %{buildroot}%{_bindir}/%{name}
install -Dp -m 644 %{name}.service %{buildroot}%{_userunitdir}/%{name}.service

%if 0%{?fedora} >= 32
%post
%systemd_user_post %{name}.service

%preun
%systemd_user_preun %{name}.service
%endif


%files
%license LICENSE
%doc README.md demo.gif
%{_bindir}/%{name}
%dir %{_userunitdir}
%{_userunitdir}/%{name}.service


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 21 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.2.1-1
- Update to 1.2.1

* Thu May 21 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.0-4
- Set all compiler and linker flags with the right macro (thanks tartina)

* Thu May 21 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.0-3
- Update PRs

* Wed May 20 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.0-2
- Fix build on s390x

* Wed May 20 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.1.0-1
- Update to 1.1.0

* Fri May  8 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.1-2
- Include demo animation as documentation
- Own /usr/lib/systemd/unit, since the service file is optional

* Wed May  6 2020 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.0.1-1
- Initial package

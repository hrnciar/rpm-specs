Name:           unifying-receiver-udev
Version:        0.2
Release:        14%{?dist}
Summary:        udev rules for user access to Logitech Unifying Receiver
License:        GPLv3
URL:            http://www.brouhaha.com/~eric/software/%{name}/
Source0:        http://www.brouhaha.com/~eric/software/%{name}/download/%{name}-%{version}.tar.gz
BuildArch:      noarch

# Adds device 046d/c52f to the udev rules, fixing bug 1202977. Rather than
# trying to submit this change upstream, a better solution is probably to use
# the udev rules shipped with solaar itself. See the bug for more details.
Patch0:         unifying-receiver-udev-046d-c52f.patch

%global udev_order 69

%global udev_rules_dir /usr/lib/udev/rules.d
# Do not use %{_libdir}, because udev rules always go into
# /usr/lib/udev/rules.d, and not (on x86_64) /usr/lib64/udev/rules.d

%description
Udev rules to allow user access to the Logitech Unifying Receiver, e.g., for
use with ltunify, pairing_tool, or Solaar.

%prep
%setup -q
%patch0 -p1

%build

%install
install -D -p -m 644 unifying-receiver.rules %{buildroot}%{udev_rules_dir}/%{udev_order}-unifying-receiver.rules

%files
%doc COPYING
%{udev_rules_dir}

%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Nov 27 2016 Richard Fearn <richardfearn@gmail.com> - 0.2-7
- Patch udev rules to add device 046d/c52f (bug #1202977)

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jul 14 2013 Eric Smith <brouhaha@fedoraproject.org> 0.2-2
- own the udev rules directory - otherwise would need conditionals for
  package dependency for udev or systemd based on distribution, or a
  file dependency on the directory

* Wed May 01 2013 Eric Smith <eric@brouhaha.com> 0.2-1
- upstream license clarification

* Sun Apr 28 2013 Eric Smith <eric@brouhaha.com> 0.1-1
- initial version

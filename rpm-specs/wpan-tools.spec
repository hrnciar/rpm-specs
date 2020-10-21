Name:          wpan-tools
Version:       0.9
Release:       5%{?dist}
Summary:       Userspace tools for the Linux IEEE 802.15.4 stack
License:       ISC
URL:           https://github.com/linux-wpan/

Source0:       https://github.com/linux-wpan/wpan-tools/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz

BuildRequires: gcc
BuildRequires: libnl3-devel

%description
Userspace tools for the Linux IEEE 802.15.4 stack.

%prep
%autosetup -p1

%build
%configure --disable-static

%make_build

%install
%make_install

%check
make %{?_smp_mflags} check

%files
%license COPYING
%doc wpan-ping/README.wpan-ping
%{_bindir}/iwpan
%{_bindir}/wpan-ping
%{_bindir}/wpan-hwsim

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 24 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.9-1
- Update to 0.9

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar  9 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.8-2
- Add gcc BR

* Sun Feb 11 2018 Peter Robinson <pbrobinson@fedoraproject.org> 0.8-1
- Update to 0.8

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Aug  7 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-5
- Fix FTBFS with libnl 3.3

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Sep 20 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.7-1
- Update to 0.7

* Wed Mar 23 2016 Peter Robinson <pbrobinson@fedoraproject.org> 0.6-1
- Update to 0.6

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sun Aug 23 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.5-1
- Update to 0.5

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Feb  3 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.4-2
- Update license, use %%license

* Mon Jan 26 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.4-1
- Update to 0.4

* Fri Jan  2 2015 Peter Robinson <pbrobinson@fedoraproject.org> 0.3-1
- Update to 0.3

* Mon Nov 17 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.2-1
- Update to 0.2

* Tue Oct 21 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-2
- Update license

* Mon Oct 20 2014 Peter Robinson <pbrobinson@fedoraproject.org> 0.1-1
- Initial package

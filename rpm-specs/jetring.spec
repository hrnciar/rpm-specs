Name:           jetring
Version:        0.29
Release:        3%{?dist}
Summary:        GPG keyring maintenance using changesets

License:        GPLv2+
URL:            http://joeyh.name/code/jetring/
Source0:        http://ftp.debian.org/debian/pool/main/j/%{name}/%{name}_%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  gnupg
BuildRequires:  perl-generators
BuildRequires:  perl(Cwd)
BuildRequires:  perl(File::Temp)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(strict)
BuildRequires:  perl(warnings)
Requires:       gnupg

%description
jetring is a collection of tools that allow for GPG keyrings to be maintained
using changesets. It was developed with the Debian keyring in mind, and aims to
solve the problem that a GPG keyring is a binary blob that's hard for multiple
people to collaboratively edit.


%prep
%autosetup -p1 -n %{name}


%build
%make_build


%install
%make_install
install -Dpm 0644 jetring.7 %{buildroot}%{_mandir}/man7/jetring.7
install -d %{buildroot}%{_mandir}/man1
install -pm 0644 jetring-*.1 %{buildroot}%{_mandir}/man1


%files
%doc README
%license GPL
%{_bindir}/jetring*
%{_mandir}/man1/*
%{_mandir}/man7/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Sep 25 2019 Sandro Mani <manisandro@gmail.com> - 0.29-1
- Update to 0.29

* Mon Sep 23 2019 Sandro Mani <manisandro@gmail.com> - 0.28-1
- Update to 0.28

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Mar 19 2018 Sandro Mani <manisandro@gmail.com> - 0.27-1
- Update to 0.27

* Wed Mar 14 2018 Sandro Mani <manisandro@gmail.com> - 0.26-1
- Update to 0.26

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Dec 17 2016 Sandro Mani <manisandro@gmail.com> - 0.25-1
- Update to 0.25

* Sun Apr 10 2016 Sandro Mani <manisandro@gmail.com> - 0.24-1
- Update to 0.24

* Sat Apr 09 2016 Sandro Mani <manisandro@gmail.com> - 0.23-1
- Update to 0.23

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jan 02 2015 Sandro Mani <manisandro@gmail.com> - 0.21-1
- Update to 0.21

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Sep 23 2013 Sandro Mani <manisandro@gmail.com> - 0.20-3
- Add manpages

* Sun Sep 22 2013 Sandro Mani <manisandro@gmail.com> - 0.20-2
- Add missing BR
- Use smp_mflags
- Use correct homepage

* Thu Sep 19 2013 Sandro Mani <manisandro@gmail.com> - 0.20-1
- Initial package

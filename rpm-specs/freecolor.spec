
Summary:	Display memory information graphically
Name:		freecolor
Version:	0.9.3
Release:	11%{?dist}

License:	MIT
URL:		http://www.rkeene.org/oss/freecolor/
Source0:	http://www.rkeene.org/files/oss/freecolor/freecolor-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
Freecolor displays the total amount of free and used physical and swap
memory in the system as a colored bargraph on the command line.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
install -Dpm 0755 free %{buildroot}/%{_bindir}/freecolor
install -Dpm 0644 freecolor.1 %{buildroot}/%{_mandir}/man1/freecolor.1


%files
%license COPYING
%doc README
%{_bindir}/freecolor
%{_mandir}/man1/*.1*


%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Denis Fateyev <denis@fateyev.com> - 0.9.3-8
- Spec cleanup, added BR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Denis Fateyev <denis@fateyev.com> - 0.9.3-1
- Update to 0.9.3 release

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Jan 21 2014 Denis Fateyev <denis@fateyev.com> - 0.9.2-1
- Initial Fedora RPM release

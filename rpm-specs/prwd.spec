Name:         prwd
Version:      1.9.1
Release:      2%{?dist}
Summary:      A tool to print a reduced working directory
License:      ISC
URL:          http://tamentis.com/projects/prwd
Source0:      http://tamentis.com/projects/%{name}/files/%{name}-%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	make

%description
Most shells read $PS1 differently and have a very rigid way to display 
the current working directory. prwd allows you to have one way to handle 
the display of your working directory and use it across multiple shells. 
It also allows you to keep an eye on your current branch when you enter 
a project handled by git or mercurial.

%prep
%setup -q
# Fix the typo here.
sed -i 's|commadn|command|g' ChangeLog

%build
%configure
%make_build

%install
%make_install

%check
make test

%files
%doc AUTHORS ChangeLog prwdrc.example TODO
%license LICENSE
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}rc.5*

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.9.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Aug 26 2019 Denis Fateyev <denis@fateyev.com> - 1.9.1-1
- Update to 1.9.1

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Jul 23 2018 Denis Fateyev <denis@fateyev.com> - 1.9-8
- Spec cleanup, added BR

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Jul 20 2015 Christopher Meng <rpm@cicku.me> - 1.9-1
- Update to 1.9

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Aug 26 2013 Christopher Meng <rpm@cicku.me> - 1.8-1
- New version.

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.7-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 1.7-2
- SPEC cleanup.

* Sun May 26 2013 Christopher Meng <rpm@cicku.me> - 1.7-1
- New version.
- Fixes for debuginfo.

* Thu May 16 2013 Christopher Meng <rpm@cicku.me> - 1.6-1
- Initial Package.

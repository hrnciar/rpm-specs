Name:		goobook
Version:	3.3
Release:	7%{?dist}
Summary:	Abook-style interface for google contacts for mutt

License:	GPLv3
URL:		https://gitlab.com/goobook/goobook
Source0:	https://pypi.python.org/packages/source/g/%{name}/%{name}-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	python3-setuptools
BuildRequires:	python3-devel

%description
Goobook is a command-line interface to Google contacts. It includes
* Searching contacts
* Mutt integration (the same way as for abook)
* Adding new contacts (very basic)

%prep
%setup -q -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

# Remove shebang
for lib in %{buildroot}%{python_sitelib}/goobook/*.py; do
	sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
	touch -r $lib $lib.new &&
	mv $lib.new $lib
done

%files
%doc LICENSE.txt README.rst CHANGES.rst CONTRIBUTORS.rst TODO.rst HACKING.rst
%{python3_sitelib}/goobook*
%{_bindir}/goobook

%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-7
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 3.3-5
- Rebuilt for Python 3.9

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 3.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3-3
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 3.3-2
- Rebuilt for Python 3.8

* Sat Aug 17 2019 Sven Lankes <sven@lank.es> - 3.3-1
- update to latest upstream release

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 05 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.9-7
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-4
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jan 26 2016 Sven Lankes <sven@lank.es> - 1.9-2
- Add missing requires for python-httplib2

* Fri Dec 25 2015 Dhiru Kholia <dhiru@openwall.com> - 1.9-1
- Update to upstream version 1.9
- Clean up the spec file

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 1.3-14
- Fix FTBFS with setuptools >= 0.7 (#992420, #1106705)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Jul 28 2011 Howard Ning <mrlhwliberty@gmail.com> - 1.3-8
- Remove argparser in the setup.py so it will work on F15

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jan 2 2011 Howard Ning <mrlhwliberty@gmail.com> - 1.3-6
- Remove argparser requirement

* Wed Aug 25 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.3-5
- Add python-setuptools requirement

* Sun Aug 8 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.3-4
- Change the version requirement.

* Fri Aug 6 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.3-3
- BuildRequires python-setuptools

* Wed Aug 4 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.3-2
- Clean up the spec file

* Sun Jul 25 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.3-1
- Bump version to official release

* Mon Jun 21 2010 Howard Ning <mrlhwliberty@gmail.com> - 1.3-0.1.a1
- Initial Release

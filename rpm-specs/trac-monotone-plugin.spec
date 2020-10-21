%global tarname	TracMonotone-%{version}
%global tardate	20100327
%global tarrev	da420c80
%global tarsfx	.%{tardate}mtn%{tarrev}

Name:		trac-monotone-plugin
Version:	0.0.14
Release:	23%{tarsfx}%{?dist}
Summary:	Monotone version control plugin for Trac
License:	GPLv2+
URL:		http://tracmtn.1erlei.de/
# Source comes from mtn right now:
#  mtn clone -r %%{tarrev} monotone.ca net.venge.monotone.trac-plugin tracmtn
#  cd tracmtn; python2 setup.py sdist --formats bztar
#  mv dist/%%{tarname}.tar.bz2 %%{tarname}%%{tarsfx}.tar.bz2
Source:		%{tarname}%{tarsfx}.tar.bz2
BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
Requires:	python2-setuptools
Requires:	trac
Requires:	monotone >= 0.46


%description
This Trac plugin provides support for the Monotone SCM.


%prep
%setup -n %{tarname} -q


%build
%py2_build


%install
%py2_install


%files
%doc README
%license COPYING
%{python2_sitelib}/*


%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-23.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-22.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-21.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-20.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Jul 15 2018 Thomas Moschny <thomas.moschny@gmx.de> - 0.0.14-19.20100327mtnda420c80
- Modernize spec file.

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-19.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.0.14-18.20100327mtnda420c80
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-17.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-16.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-15.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.0.14-14.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-13.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-12.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-11.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-10.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-9.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-8.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-7.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 0.0.14-6.20100327mtnda420c80
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Apr 11 2010 Thomas Moschny <thomas.moschny@gmx.de> - 0.0.14-5.20100327mtnda420c80
- Update to current head, in order to support monotone >= 0.46.
- Remove old conditionals.
- Use %%global instead of %%define.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-4.20080208mtnb4dd178b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.0.14-3.20080208mtnb4dd178b
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.0.14-2.20080208mtnb4dd178b
- Rebuild for Python 2.6

* Fri Feb  8 2008 Roland McGrath <roland@redhat.com> - 0.0.14-1.20080208mtnb4dd178b
- New upstream version.

* Tue Feb  5 2008 Roland McGrath <roland@redhat.com> - 0.0.14-1.20080205mtn8ef4880f
- New upstream version.

* Fri Jan 25 2008 Roland McGrath <roland@redhat.com> - 0.0.13-1.20080125mtn393b5412
- New upstream version, fixes errors in log/ urls.

* Fri Jan 18 2008 Roland McGrath <roland@redhat.com> - 0.0.12-1.20080116mtn3907adc7
- New package

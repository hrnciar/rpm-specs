Name:           latex-mk
Version:        2.1
Release:        15%{?dist}
Summary:        Makefile fragments and shell scripts for latex

License:        BSD
URL:            http://latex-mk.sourceforge.net/
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz


BuildArch:      noarch
# for /usr/bin/texi2dvi
BuildRequires:  texinfo-tex


%description
LaTeX-Mk is a collection of makefile fragments and shell scripts for
simplifying the management of small to large sized LaTeX documents.


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


#%check
#pushd testsuite
#GMAKE=make ./run_tests.sh --without-bmake
#popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT
mkdir fedora-doc
mv $RPM_BUILD_ROOT/%{_datadir}/latex-mk/latex-mk.* fedora-doc
mv $RPM_BUILD_ROOT/%{_datadir}/latex-mk/example fedora-doc
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/
echo 'export LATEX_MK_DIR=%{_datadir}/latex-mk' > $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/latex-mk.sh
echo 'setenv LATEX_MK_DIR %{_datadir}/latex-mk' > $RPM_BUILD_ROOT/%{_sysconfdir}/profile.d/latex-mk.csh
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%doc AUTHORS COPYING ChangeLog NEWS README TODO fedora-doc/*
%config %{_sysconfdir}/profile.d/latex-mk.sh
%config %{_sysconfdir}/profile.d/latex-mk.csh
%{_bindir}/ieee-copyout
%{_bindir}/latex-mk
%{_datadir}/latex-mk/
%{_infodir}/latex-mk.info*


%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri May 13 2011 Till Maas <opensource@till.name> - 2.1-1
- Update to new release

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Apr 14 2010 Till Maas <opensource@till.name> - 2.0-1
- Update to new release
- Add texinfo-tex BR
- Do not hardcopy info compression suffix

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jul 28 2007 - Till Maas <opensource till name> - 1.9-1
- update to new version
- change Source0: to recommended sf.net URL
- add enviroment for csh

* Fri Mar 09 2007 - Till Maas <opensource till name> - 1.8-2
- remove %%{_infodir}/dir because it is created sometimes

* Wed Feb 07 2007 - Till Maas <opensource till name> - 1.8-1
- initial spec for Fedora Extras

%define _dataset yale5

Summary:	Stellar data set for use by the StarPlot tool
Name:		starplot-%{_dataset}
Version:	0.95
Release:	20%{?dist}
License:	Redistributable, no modification permitted
URL:		http://starplot.org/
Source0:	http://starplot.org/data/%{_dataset}-%{version}.tar.gz


Requires:	starplot >= %{version}
Requires(post):	starplot >= %{version}

BuildArch:	noarch

%description
Stellar data set for use by the StarPlot tool from the [Yale] Bright Star
Catalog, 5th Rev. Ed. (preliminary), Hoffleit and Warren, 1991. The data set
was obtained from the archives of the Astronomical Data Center (ADC) at NASA
Goddard Space Flight Center.

%prep
%setup -q -n %{_dataset}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data

install -p -m644 %{_dataset}.spec \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}
install -p -m644 orig-data/catalog.dat \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data
install -p -m644 orig-data/notes.dat \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data
install -p -m644 orig-data/ReadMe \
  $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}/orig-data

touch $RPM_BUILD_ROOT%{_datadir}/starplot/%{_dataset}.stars

%post
starpkg --dataset %{_datadir}/starplot/%{_dataset} --dest %{_datadir}/starplot

%files
%doc Changelog
%doc COPYING
%doc README
%ghost %{_datadir}/starplot/%{_dataset}.stars

%dir %{_datadir}/starplot/%{_dataset}
%{_datadir}/starplot/%{_dataset}/%{_dataset}.spec
%{_datadir}/starplot/%{_dataset}/orig-data

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.95-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.95-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Dec 25 2007 Parag Nemade <paragn@fedoraproject.org> - 0.95-2
- Fixed installation error with --excludedocs.

* Sun Dec 16 2007 Debarshi Ray <rishi@fedoraproject.org> - 0.95-1
- Initial build.

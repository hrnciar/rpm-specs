%define mainversion 2.0
%define extra 0.2.0

Name:           PySolFC-cardsets
Version:        2.0
Release:        20%{?dist}
Summary:        Various cardsets for PySolFC
License:        GPLv2+
URL:            https://pysolfc.sourceforge.io/
Source0:        https://github.com/shlomif/PySolFC-Cardsets/archive/%{version}/PySolFC-Cardsets-%{version}.tar.gz
Source1:        https://github.com/shlomif/PySol-Extra-Mahjongg-Cardsets/archive/%{extra}/PySol-Extra-Mahjongg-Cardsets-%{extra}.tar.gz
BuildArch:      noarch

Requires:       PySolFC >= %{mainversion}

%description
This package contains extras cardsets for PySolFC.

%prep
%setup -q -n PySolFC-Cardsets-%{version} -a1

%build

%install
install -d -m755 $RPM_BUILD_ROOT%{_datadir}/PySolFC
# remove cardsets included in PySolFC package
rm -rf cardset-2000 cardset-crystal-mahjongg cardset-dashavatara-ganjifa \
       cardset-dondorf cardset-gnome-mahjongg-1 cardset-hexadeck \
       cardset-kintengu cardset-matrix cardset-mughal-ganjifa cardset-oxymoron \
       cardset-standard cardset-tuxedo cardset-vienna-2k cardset-hanafuda-200-years
cp -a cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC
cp -a PySol-Extra-Mahjongg-Cardsets-0.2.0/Lost-Mahjongg-Cardsets/cardset-* $RPM_BUILD_ROOT%{_datadir}/PySolFC


find $RPM_BUILD_ROOT%{_datadir}/PySolFC -type f -name 'COPYRIGHT' -exec chmod 0644 '{}' \;

%files
%{_datadir}/PySolFC/cardset-*

%changelog
* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jul 24 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue May 21 2019 Sérgio Basto <sergio@serjux.com> - 2.0-18
- Add Lost-Mahjongg-Cardsets

* Mon May 06 2019 Sérgio Basto <sergio@serjux.com> - 2.0-17
- Use new github sources

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Jun 16 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Fri Jun 06 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Aug 02 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb 10 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-3
- Change requirement on main version to >= 2.0, not = 1.1

* Mon Feb 8 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-2
- Add dist tag since manual copying is not done anymore (see releng #3335)

* Sat Jan 30 2010 Stewart Adam <s.adam at diffingo.com> - 2.0-1
- Update to 2.0

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Feb 23 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-4.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Oct 25 2007 Stewart Adam <s.adam@diffingo.com> 1.1-3
- Remove BR python-devel
- Add dot to %%description
- Remove preinstalled cardsets
- Use a dir PySolFC actually recognizes

* Wed Oct 24 2007 Stewart Adam <s.adam@diffingo.com> 1.1-2
- Own dirs we create
- Remove %%{?dist} tag
- Fix URL, description and summary
- Don't place any executable files in the RPM

* Sat Sep 29 2007 Stewart Adam <s.adam@diffingo.com> 1.1-1
- Initial release

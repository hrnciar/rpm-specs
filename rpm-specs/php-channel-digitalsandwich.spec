%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}

Name:		php-channel-digitalsandwich
# Use REST version (from channel.xml)
Version:	1.3
Release:	16%{?dist}
Summary:	Adds digitalsandwich channel to PEAR

License:	Public Domain
URL:		http://digitalsandwich.com/
Source0:	http://pear.digitalsandwich.com/channel.xml

BuildArch:	noarch
BuildRequires:	php-pear >= 1:1.4.9-1.2
Requires:	php-pear(PEAR)

Requires(post): %{__pear}
Requires(postun): %{__pear}

Provides:	php-channel(pear.digitalsandwich.com)

%description
This package adds the digitalsandwich channel which allows
PEAR packages from this channel to be installed.

%prep
%setup -q -c -T


%build
# Empty build section, nothing to build


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{pear_xmldir}
install -pm 644 %{SOURCE0} $RPM_BUILD_ROOT%{pear_xmldir}/pear.digitalsandwich.com.xml


%post
if [ $1 -eq  1 ] ; then
	%{__pear} channel-add %{pear_xmldir}/pear.digitalsandwich.com.xml > /dev/null || :
else
	%{__pear} channel-update %{pear_xmldir}/pear.digitalsandwich.com.xml > /dev/null ||:
fi


%postun
if [ $1 -eq 0 ] ; then
	%{__pear} channel-delete pear.digitalsandwich.com > /dev/null || :
fi


%files
%{pear_xmldir}/*


%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 21 2012 Christof Damian <christof@damian.net> - 1.3-2
- fixes for review:
- remove php-cli from requires
- change license to Public Domain
- clean unneeded macros (rm, install, mkdir)

* Wed May  2 2012 Christof Damian <christof@damian.net> - 1.3-1
- initial release


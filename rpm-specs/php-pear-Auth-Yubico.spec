%{!?__pear: %{expand: %%global __pear %{_bindir}/pear}}
%{!?pear_metadir: %global pear_metadir %{pear_phpdir}}

%global pear_name	Auth_Yubico
%global channel		__uri

Name:		php-pear-Auth-Yubico
Version:	2.5
Release:	11%{?dist}
Summary:	Authentication class for verifying Yubico OTP tokens

License:	BSD
URL:		https://developers.yubico.com/php-yubico/
Source0:	https://developers.yubico.com/php-yubico/Releases/Auth_Yubico-%{version}.tgz
Patch1:		php-pear-Auth-Yubico-2.3.channel.patch
BuildArch:	noarch
BuildRequires:	php-pear >= 1:1.4.9-1.2

Requires:	php-pear(PEAR) >= 1.4.0
Requires(post):		%{__pear}
Requires(postun):	%{__pear}

Provides:	php-pear(%{channel}/%{pear_name}) = %{version}


%description
  The Yubico authentication PHP class provides an easy way to integrate the
Yubikey into your existing PHP-based user authentication infrastructure.


#-------------------------------------------------------------------------------
%prep
#-------------------------------------------------------------------------------

%setup -q -n Auth_Yubico-%{version}
%patch1 -p 1

#	Create a "localized" php.ini to avoid install warnings.

cp /etc/php.ini .
echo 'date.timezone=UTC' >> php.ini

#	Fix end of line encoding.

for file in Modhex_Calculator.php Modhex.php
do	sed -i -e 's/\r$//' "example/${file}"
done


#-------------------------------------------------------------------------------
%build
#-------------------------------------------------------------------------------

#	Nothing to do.


#-------------------------------------------------------------------------------
%install
#-------------------------------------------------------------------------------

rm -rf "${RPM_BUILD_ROOT}"

PHPRC=php.ini	%{__pear} install --nodeps				\
				--packagingroot "${RPM_BUILD_ROOT}"	\
				package.xml

#	Clean up unnecessary files.

rm -rf "${RPM_BUILD_ROOT}%{pear_metadir}/".??*

#	Install XML package description.

mkdir -p "${RPM_BUILD_ROOT}%{pear_xmldir}"
install -p -m 644 package.xml "${RPM_BUILD_ROOT}%{pear_xmldir}/%{name}.xml"

#-------------------------------------------------------------------------------
%post
#-------------------------------------------------------------------------------

%{__pear} install --nodeps --soft --force --register-only		\
	"%{pear_xmldir}/%{name}.xml" > /dev/null || :


#-------------------------------------------------------------------------------
%postun
#-------------------------------------------------------------------------------

if [ "${1}" -eq "0" ]
then	%{__pear} uninstall --nodeps --ignore-errors --register-only	\
		"%{channel}/%{pear_name}" > /dev/null || :
fi


#-------------------------------------------------------------------------------
%files
#-------------------------------------------------------------------------------

%defattr(-, root, root, -)
%doc NEWS README COPYING
%doc example demo.php
%{pear_xmldir}/%{name}.xml
%{pear_phpdir}/Auth


#-------------------------------------------------------------------------------
%changelog
* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

#-------------------------------------------------------------------------------

* Wed May 13 2015 Patrick Monnerat <pm@datasphere.ch> 2.5-1
- New upstream release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Patrick Monnerat <pm@datasphere.ch> 2.4-3
- Use new pear_metadir macro.

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Mar 28 2012 Patrick Monnerat <pm@datasphere.ch> 2.4-1
- New upstream release.

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 21 2011 Patrick Monnerat <pm@datasphere.ch> 2.3-2
- Some spec file adjustments:
  https://bugzilla.redhat.com/show_bug.cgi?id=675122#c1

* Thu Feb  3 2011 Patrick Monnerat <pm@datasphere.ch> 2.3-1
- Initial rpm packaging.
- Patch "channel" to change package channel in XML description file.

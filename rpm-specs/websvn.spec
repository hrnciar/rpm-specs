Name:           websvn
Version:        2.3.3
Release:        20%{?dist}
Summary:        Online subversion repository browser

License:        GPLv2+
URL:            http://www.websvn.info
Source0:        http://websvn.tigris.org/files/documents/1380/49056/websvn-2.3.3.tar.gz
Source1:        websvn-httpd.conf
Patch1:         websvn-2.3.3-use_system_libs.patch
# https://bugs.debian.org/cgi-bin/bugreport.cgi?msg=5;filename=websvn_symlinks.patch;att=1;bug=775682
Patch2:         websvn-2.3.3-CVE-2013-6892.patch
Patch3:         websvn-2.3.3-CVE-2016-2511.patch
Patch4:         websvn-2.3.3-CVE-2016-1236.patch
BuildArch:      noarch

Requires(pre):  httpd
Requires:       sed
Requires:       enscript
Requires:       php >= 4.3.0
Requires:       php-mbstring
Requires:       php-xml
Requires:       php-geshi
Requires:       php-pear(Archive_Tar)
Requires:       php-pear(Text_Diff)


%description
WebSVN offers a view onto your subversion repositories that's been designed to
reflect the Subversion methodology. You can view the log of any file or
directory and see a list of all the files changed, added or deleted in any
given revision. You can also view the differences between two versions of a
file so as to see exactly what was changed in a particular revision.


%package selinux
Summary:          SELinux context for %{name}
Requires:         %name = %version-%release
Requires(post):   policycoreutils
Requires(postun): policycoreutils


%description selinux
SElinux context for %{name}.


%prep
%setup -q
### Let websvn use the system provided php classes and remove bundled ones.
%patch1 -p1
rm -rf lib/
# CVE-2013-6892
%patch2 -p1
# CVE-2016-2511
%patch3 -p1
# CVE-2016-1236.patch
%patch4 -p1

mv include/distconfig.php include/config.php
find templates/calm -type f -exec chmod -R a-x {} ';'
sed -i -e 's/\r//' doc/style.css
iconv -f iso8859-1 -t utf-8 changes.txt > changes.txt.conv \
&& touch -r changes.txt changes.txt.conv \
&& mv -f changes.txt.conv changes.txt
sed -i -e "s#^\$locwebsvnhttp = '';#\$locwebsvnhttp = '/websvn';#" wsvn.php
sed -i -e "s#^\/\/ \$config->useMultiViews();#\$config->useMultiViews();#" \
    include/config.php


%build
# Nothing to build


%install
rm -rf $RPM_BUILD_ROOT

# Install the code
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a *.php include javascript languages templates \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}

# Move the conf to the proper place
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
mv $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php \
   $RPM_BUILD_ROOT/%{_sysconfdir}/%{name}
ln -s ../../../..%{_sysconfdir}/%{name}/config.php \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/include/config.php

# Apache conf
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d
install -m 0644 %{SOURCE1} \
                $RPM_BUILD_ROOT/%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Move the cache dir to a better place
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/cache/%{name}
ln -s ../../..%{_localstatedir}/cache/%{name} \
   $RPM_BUILD_ROOT/%{_datadir}/%{name}/cache

# Move the temp dir to a better place
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/tmp
ln -s ../../..%{_localstatedir}/tmp $RPM_BUILD_ROOT/%{_datadir}/%{name}/temp



%post selinux
semanage fcontext -a -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
restorecon -R %{_localstatedir}/cache/%{name} || :


%postun selinux
if [ $1 -eq 0 ] ; then
semanage fcontext -d -t httpd_cache_t '%{_localstatedir}/cache/%{name}(/.*)?' 2>/dev/null || :
fi


%files
%doc changes.txt license.txt doc/
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%config(noreplace) %{_sysconfdir}/%{name}/config.php
%{_datadir}/%{name}
%attr(-,apache,root) %{_localstatedir}/cache/%{name}


%files selinux


%changelog
* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu May 12 2016 Xavier Bachelot <xavier@bachelot.org> 2.3.3-13
- Add patch for CVE-2016-1236 (RHBZ#1333673).

* Tue Mar 01 2016 Xavier Bachelot <xavier@bachelot.org> 2.3.3-12
- Add patch for CVE-2016-2511 (RHBZ#1310758).

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.3.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed May 06 2015 Xavier Bachelot <xavier@bachelot.org> 2.3.3-9
- Add missing javascript directory (RHBZ#1218590).

* Wed Jan 21 2015 Xavier Bachelot <xavier@bachelot.org> 2.3.3-8
- Add patch for CVE-2013-6892 (RHBZ#1183632).

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Dec 02 2012 Johan Cwiklinski <johan AT x-tnd DOT be> - 2.3.3-4
- Fix apache 2.4 configuration (bz #871495)

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Jun 28 2011 Xavier Bachelot <xavier@bachelot.org> 2.3.3-1
- Update to 2.3.3.

* Tue Mar 01 2011 Xavier Bachelot <xavier@bachelot.org> 2.3.2-1
- Update to 2.3.2.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Sep 27 2010 Xavier Bachelot <xavier@bachelot.org> 2.3.1-2
- Add an selinux subpackage for compatibility with selinux (RHBZ#585969).

* Tue Jun 15 2010 Xavier Bachelot <xavier@bachelot.org> 2.3.1-1
- Update to 2.3.1.

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May 22 2009 Xavier Bachelot <xavier@bachelot.org> 2.2.1-1
- Update to 2.2.1.
- Preserve time stamp when fixing encoding.

* Sat May 09 2009 Xavier Bachelot <xavier@bachelot.org> 2.2.0-2
- php-pear(Text_Diff) is mandatory now.
- Add Requires(pre): httpd.

* Thu Apr 23 2009 Xavier Bachelot <xavier@bachelot.org> 2.2.0-1
- Update to 2.2.0.
- Actually use the system provided classes.
- Add Requires: php-pear(Archive_Tar).
- Remove implicit Requires: php-common.

* Thu Mar 26 2009 Xavier Bachelot <xavier@bachelot.org> 2.1.0-3
- Turn multiview on by default.

* Thu Mar 26 2009 Xavier Bachelot <xavier@bachelot.org> 2.1.0-2
- More Requires:.
- Move temp and cache dir to a better place.
- Set a proper locwebsvnhttp in wsvn.php.

* Wed Mar 18 2009 Xavier Bachelot <xavier@bachelot.org> 2.1.0-1
- Initial build.

%if "%{php_version}" < "5.6"
%global ini_name     facedetect.ini
%else
%global ini_name     40-facedetect.ini
%endif

%global github_owner    infusion
%global github_name     PHP-Facedetect
%global github_commit   135c72ace26cd95fd5fd255053bc2eb694d87ad9
%global commitdate      20200129
%global shortcommit     %(c=%{github_commit}; echo ${c:0:7})

Name:		php-facedetect
Version:	1.2.0
Release:	0.17.%{commitdate}git%{shortcommit}%{?dist}
Summary:	PHP extension to access the OpenCV library
License:	BSD
URL:		http://www.xarg.org/project/php-facedetect/
Source0:	https://github.com/%{github_owner}/%{github_name}/archive/%{github_commit}/%{github_name}-%{shortcommit}.tar.gz
# https://github.com/infusion/PHP-Facedetect/pull/37
Patch0:	PHP-Facedetect-opencv_fix.patch

BuildRequires:	gcc-c++
BuildRequires:	php-devel
BuildRequires:	pkgconfig(opencv) >= 3.0.0
Requires:	opencv
Requires:	php(zend-abi) = %{php_zend_api}
Requires:	php(api) = %{php_core_api}


%description
This extension provides a PHP implementation of the OpenCV library.
The extension offers two new functions. In principle, they differ
only by their return value. The first returns only the number of
faces found on the given image and the other an associative array
of their coordinates.


%prep
%autosetup -n %{github_name}-%{github_commit}
sed -i -e 's/includedir_new/includedir/g' config.m4

%{__cat} <<'EOF' >%{ini_name}
extension=facedetect.so
EOF
sed -i 's/\r//' CREDITS

%build
phpize
%configure
make %{?_smp_mflags}

%install 
make install INSTALL_ROOT=$RPM_BUILD_ROOT INSTALL="install -p" 
install -p -D -m0644 %{ini_name} $RPM_BUILD_ROOT%{_sysconfdir}/php.d/%{ini_name}

%check
# Minimal load test of php extension
php --no-php-ini \
    --define extension_dir=${RPM_BUILD_ROOT}%{php_extdir} \
    --define extension=facedetect.so \
    --modules | grep facedetect

%files
%doc CREDITS
%license LICENSE
%config(noreplace) %{_sysconfdir}/php.d/%{ini_name}
%{php_extdir}/facedetect.so

%changelog
* Tue Oct 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.17.20200129git135c72a
- Fix build with opencv 4.5.0

* Tue Oct 20 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.16.20200129git135c72a
- Update snapshot

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.15.20180306gitc717941
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.14.20180306gitc717941
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Jun 04 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.13.20180306gitc717941
- Rebuilt for OpenCV 4.3

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.12.20180306gitc717941
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Tue Jan 28 2020 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.11.20180306gitc717941
- Rebuild for OpenCV 4.2

* Sun Dec 29 2019 Nicolas Chauvet <kwizart@gmail.com> - 1.2.0-0.10.20180306gitc717941
- Rebuilt for opencv4

* Fri Oct 04 2019 Remi Collet <remi@remirepo.net> - 1.2.0-0.9.20180306gitc717941
- rebuild for https://fedoraproject.org/wiki/Changes/php74

* Wed Sep 11 2019 Mamoru TASAKA <mtasaka@fedoraproject.org> - 1.2.0-0.8.20180306gitc717941
- Rebuild for opencv (with vtk disabled)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.7.20180306gitc717941
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.6.20180306gitc717941
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 11 2018 Remi Collet <remi@remirepo.net> - 1.2.0-0.5.20180306gitc717941
- Rebuild for https://fedoraproject.org/wiki/Changes/php73

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-0.4.20180306gitc717941
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Sérgio Basto <sergio@serjux.com> - 1.2.0-0.3.20180306gitc717941
- Fix the License tag

* Thu Mar 15 2018 Sérgio Basto <sergio@serjux.com> - 1.2.0-0.2.20180306gitc717941
- Add last commit

* Mon Mar 05 2018 Adam Williamson <awilliam@redhat.com> - 1.2.0-0.1.20180305git263435f
- Bump to latest git (PHP 7, OpenCV 3.x compat)
- BuildRequires gcc-c++
- License change back to PHP

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Dec 24 2017 Sérgio Basto <sergio@serjux.com> - 1.1.0-10
- Rebuild (opencv-3.3.1)

* Tue Oct 03 2017 Remi Collet <remi@fedoraproject.org> - 1.1.0-9
- rebuild for https://fedoraproject.org/wiki/Changes/php72

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Mar 03 2017 Sérgio Basto <sergio@serjux.com> - 1.1.0-6
- Rebuild (opencv)

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Nov 24 2016 Remi Collet <remi@fedoraproject.org> - 1.1.0-4
- add patch to use pkg-config to retrieve build options

* Wed Jun 29 2016 Sérgio Basto <sergio@serjux.com> - 1.1.0-2
- Rebuild for PHP 7

* Sat May 07 2016 Sérgio Basto <sergio@serjux.com> - 1.1.0-1
- Update php-facedetect to 1.1.0
- Drop patch 3 is upstreamed.
- Drop patch 1 and 2 looks like that is fixed.
- Add last 8 commits from GIT upstream (change license and add opencv3 support
  which drop opencv2 support so we need just apply part2 when we have opencv3
  in buildroot)

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Fri Jun 20 2014 Remi Collet <rcollet@redhat.com> - 1.0.1-12
- rebuild for https://fedoraproject.org/wiki/Changes/Php56
- add numerical prefix to extension configuration file

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Mar 22 2013 Remi Collet <rcollet@redhat.com> - 1.0.1-9
- rebuild for http://fedoraproject.org/wiki/Features/Php55

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 Remi Collet <remi@fedoraproject.org> - 1.0.1-6
- build against php 5.4.0
- add filter to fix private-shared-object-provides
- add %%check for php extension

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Aug 31 2011 Rex Dieter <rdieter@fedoraproject.org> 1.0.1-4
- rebuild (opencv)

* Tue May 10 2011 Tom Callaway <spot@fedoraproject.org> - 1.0.1-3
- Clean up spec
- Fix code to work with OpenCV 2.2.0

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 10 2011 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.1-1
- Bump up to latest upstream
- Rebuild with new opencv

* Wed Jun 30 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.0-6
- Rebuild with new opencv

* Thu Mar 04 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.0-5
- Explicit requires opencv

* Mon Mar 01 2010 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.0-4
- Patch to build with new DSO linkage Change
- Rebuild with new opencv

* Sun Nov 29 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.0-3
- Rebuild with new opencv

* Thu Jul 30 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.0-2
- Fix macros

* Wed Jul 22 2009 Andrew Colin Kissa <andrew@topdog.za.net> - 1.0.0-1
- Initial package

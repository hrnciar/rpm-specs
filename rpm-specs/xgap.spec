Name:           xgap
Version:        4.30
Release:        6%{?dist}
Summary:        GUI for GAP

License:        GPLv2+
URL:            https://gap-packages.github.io/xgap/
Source0:        https://github.com/gap-packages/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
# Created by Jerry James <loganjerry@gmail.com>
Source1:        %{name}.desktop
# Created by Paulo César Pereira de Andrade
# <paulo.cesar.pereira.de.andrade@gmail.com>
Source2:        XGap
# Sent upstream 9 May 2012.  This patch quiets some compiler warnings.
Patch0:         %{name}-warning.patch
# Add missing escapes to buildman.pe
Patch1:         %{name}-buildman.patch
# Fix computation of GAParch
Patch2:         %{name}-gaparch.patch

BuildRequires:  desktop-file-utils
BuildRequires:  gap-devel
BuildRequires:  gcc
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  tex(manfnt.tfm)
BuildRequires:  tth

Requires:       gap%{?_isa}

Provides:       gap-pkg-xgap = %{version}-%{release}

%description
A X Windows GUI for GAP.

%package doc
Summary:        XGap documentation
BuildArch:      noarch
Requires:       %{name} = %{version}-%{release}
Requires:       gap-online-help

%description doc
This package contains documentation for %{name}.

%prep
%autosetup -p0

# Autoloading this package interferes with SAGE (bz 819705).
sed -i "/^Autoload/s/true/false/" PackageInfo.g 

# Remove references to obsolete GAP manuals
sed -i '/prg/d;/ext/d' doc/manual.tex

%build
export CFLAGS="$RPM_OPT_FLAGS -D_FILE_OFFSET_BITS=64 -D_GNU_SOURCE"
%configure --with-gaproot=%{_gap_dir}
make %{?_smp_mflags}

# Fix a path in the shell wrapper
sed -i "s,$PWD,\$GAP_DIR/pkg/%{name}-%{version}," bin/xgap.sh

# Link to main GAP documentation
ln -s %{_gap_dir}/etc ../../etc
ln -s %{_gap_dir}/doc ../../doc
ln -s %{name}-%{version} ../%{name}
make -C doc manual
rm -f ../%{name} ../../{doc,etc}

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_gap_dir}/pkg/%{name}-%{version}
cp -a *.g bin doc examples htm lib %{buildroot}%{_gap_dir}/pkg/%{name}-%{version}
rm -f %{buildroot}%{_gap_dir}/pkg/%{name}-%{version}/doc/*.{aux,bbl,blg,brf,idx,ilg,ind,log,out,pnr}
rm -f %{buildroot}%{_gap_dir}/pkg/%{name}-%{version}/doc/{buildman.*,Makefile,make_doc}
mv %{buildroot}%{_gap_dir}/pkg/%{name}-%{version}/bin/xgap.sh \
   %{buildroot}%{_bindir}/xgap
rm -f %{buildroot}%{_gap_dir}/pkg/%{name}-%{version}/bin/*/{Makefile,config*,*.o}

# Install the desktop file
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --mode=644 --dir=%{buildroot}%{_datadir}/applications \
  %{SOURCE1}

# Install the X resource file
mkdir -p %{buildroot}%{_datadir}/X11/app-defaults
cp -p %{SOURCE2} %{buildroot}%{_datadir}/X11/app-defaults

%files
%doc CHANGES README
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/X11/app-defaults/XGap
%{_gap_dir}/pkg/%{name}-%{version}/
%exclude %{_gap_dir}/pkg/%{name}-%{version}/doc/
%exclude %{_gap_dir}/pkg/%{name}-%{version}/examples/
%exclude %{_gap_dir}/pkg/%{name}-%{version}/htm/

%files doc
%docdir %{_gap_dir}/pkg/%{name}-%{version}/doc/
%docdir %{_gap_dir}/pkg/%{name}-%{version}/examples/
%docdir %{_gap_dir}/pkg/%{name}-%{version}/htm/
%{_gap_dir}/pkg/%{name}-%{version}/doc/
%{_gap_dir}/pkg/%{name}-%{version}/examples/
%{_gap_dir}/pkg/%{name}-%{version}/htm/

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.30-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Thu Mar 12 2020 Jerry James <loganjerry@gmail.com> - 4.30-5
- Rebuild for gap 4.11.0

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 4.30-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Jul 27 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.30-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jun 25 2019 Jerry James <loganjerry@gmail.com> - 4.30-2
- Require gap, not gap-core, so the binary can be invoked and the icon be seen

* Wed Apr 24 2019 Jerry James <loganjerry@gmail.com> - 4.30-1
- New upstream release

* Mon Feb  4 2019 Jerry James <loganjerry@gmail.com> - 4.29-3
- Rebuild for gap 4.10.0
- Add -buildman patch
- Add -doc subpackage

* Sun Feb 03 2019 Fedora Release Engineering <releng@fedoraproject.org> - 4.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Nov 15 2018 Jerry James <loganjerry@gmail.com> - 4.29-1
- New upstream release

* Mon Sep 24 2018 Jerry James <loganjerry@gmail.com> - 4.28-1
- New upstream release

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.27-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 22 2018 Jerry James <loganjerry@gmail.com> - 4.27-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 4.26-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.26-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.26-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Nov  7 2016 Jerry James <loganjerry@gmail.com> - 4.26-1
- New upstream release

* Sat Jul 30 2016 Jerry James <loganjerry@gmail.com> - 4.24-1
- New upstream release
- New URLs

* Thu Apr  7 2016 Jerry James <loganjerry@gmail.com> - 4.23-13
- Rebuild for gap 4.8.3

* Fri Feb 05 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.23-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Nov 11 2015 Jerry James <loganjerry@gmail.com> - 4.23-11
- Simplify scriptlets; gap-core now uses rpm file triggers
- Rebuild documentation from source

* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jan 24 2015 Jerry James <loganjerry@gmail.com> - 4.23-9
- Silence scriptlets when uninstalling
- Mark some content as documentation

* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Jerry James <loganjerry@gmail.com> - 4.23-5
- Build with large file support

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Sep 17 2012 Jerry James <loganjerry@gmail.com> - 4.23-3
- Rebuild for GAP 4.5

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.23-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed May  9 2012 Jerry James <loganjerry@gmail.com> - 4.23-1
- New upstream release
- Fix bz 819705 issues:
- Fix xgap shell script
- Install X11 resource file
- Turn off autoloading, as that interferes with SAGE

* Mon Apr 23 2012 Jerry James <loganjerry@gmail.com> - 4.22-1
- New upstream release
- Add gap-devel BR to get _gap_dir and _gap_arch_dir macros

* Wed Mar 28 2012 Jerry James <loganjerry@gmail.com> - 4.21-3
- Fix binary permissions

* Fri Feb 17 2012 Jerry James <loganjerry@gmail.com> - 4.21-2
- Add desktop file
- Fix inconsistent macro use

* Mon Jan 23 2012 Jerry James <loganjerry@gmail.com> - 4.21-1
- Initial RPM

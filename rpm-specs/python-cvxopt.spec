%global srcname cvxopt

Name:           python-%{srcname}
Version:        1.2.5
Release:        2%{?dist}
Summary:        A Python Package for Convex Optimization
License:        GPLv3+
URL:            http://cvxopt.org/
Source0:        https://github.com/%{srcname}/%{srcname}/archive/%{version}/%{srcname}-%{version}.tar.gz
# Use the openblas library instead of the system BLAS.
Patch0:         %{name}-setup.patch

BuildRequires:  DSDP-devel
BuildRequires:  fontawesome-fonts-web
BuildRequires:  font(fontawesome)
BuildRequires:  font(lato)
BuildRequires:  font(robotoslab)
BuildRequires:  fontconfig
BuildRequires:  gcc
BuildRequires:  glpk-devel
BuildRequires:  openblas-devel
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(gsl)
BuildRequires:  python3-devel
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)
BuildRequires:  suitesparse-devel
BuildRequires:  tex-dvipng
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex(latex)
BuildRequires:  tex(tex4ht.sty)
BuildRequires:  tex(utf8x.def)

Requires:       fontawesome-fonts-web
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%global _desc %{expand:
CVXOPT is a free software package for convex optimization based on
the Python programming language. Its main purpose is to make the
development of software for convex optimization applications
straightforward by building on Python's extensive standard library and
on the strengths of Python as a high-level programming language.}

%description %_desc


%package -n     python3-%{srcname}
Summary:        A Python3 Package for Convex Optimization
Provides:       bundled(jquery)
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_desc


%package        examples
Summary:        Examples of using %{name}
Requires:       python3-%{srcname} = %{version}-%{release}
Requires:       python3dist(matplotlib)
BuildArch:      noarch


%description    examples
Examples of using %{name}.


%prep
%autosetup -p0 -n %{srcname}-%{version}

# Fix library path
if [ "%{_lib}" != "lib" ]; then
  sed -i "s|%{_prefix}/lib|%{_libdir}|" setup.py
fi

# Don't use the bundled sphinx_rtd_theme
rm -fr doc/source/.themes
sed -i 's/html_theme_path/#&/' doc/source/conf.py

# Do not use env
sed -i 's,bin/env python,bin/python3,' examples/filterdemo/filterdemo_{cli,gui}

# Remove useless executable bits
find examples -name \*.py -perm /0111 | xargs chmod a-x


%build
export CC="gcc"
export LDSHARED="gcc -shared $RPM_LD_FLAGS"
%py3_build

# Rebuild the documentation
make -C doc clean
make -C doc -B html
rm -f doc/build/html/.buildinfo

# Do not bundle fonts into the documentation
cd doc/build/html/_static/fonts
for suffix in eot svg ttf woff woff2; do
  rm fontawesome-webfont.$suffix
  ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.$suffix .
done
rm {Lato,RobotoSlab}/*.ttf
ln -s $(fc-match -f "%%{file}" "lato:bold") Lato/lato-bold.ttf
ln -s $(fc-match -f "%%{file}" "lato:bold:italic") Lato/lato-bolditalic.ttf
ln -s $(fc-match -f "%%{file}" "lato:italic") Lato/lato-italic.ttf
ln -s $(fc-match -f "%%{file}" "lato") Lato/lato-regular.ttf
ln -s $(fc-match -f "%%{file}" "robotoslab:bold") RobotoSlab/roboto-slab-v7-bold.ttf
ln -s $(fc-match -f "%%{file}" "robotoslab") RobotoSlab/roboto-slab-v7-regular.ttf
cd -

%install
%py3_install

%check
PYTHONPATH=%{buildroot}%{python3_sitearch} pytest


%files -n python3-%{srcname}
%doc doc/build/html/
%license LICENSE
%{python3_sitearch}/%{srcname}*

%files examples
%doc examples/

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.2.5-2
- Rebuilt for Python 3.9

* Fri Apr 17 2020 Jerry James <loganjerry@gmail.com> - 1.2.5-1
- Version 1.2.5
- Drop upstreamed -parens patch
- Use fc-match to find fonts more robustly

* Sat Feb 29 2020 Jerry James <loganjerry@gmail.com> - 1.2.4-4
- Add -parens patch to fix build with python 3.9

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Jan 27 2020 Jerry James <loganjerry@gmail.com> - 1.2.4-2
- Reenable s390x tests now that DSDP has been fixed

* Fri Jan 24 2020 Jerry James <loganjerry@gmail.com> - 1.2.4-1
- Version 1.2.4
- Drop upstreamed -bool patch
- Unbundle sphinx_rtd_theme
- Unbundle fonts from the documentation
- Temporarily disable tests on s390x until probable DSDP bug can be diagnosed

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-6
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Wed Aug 21 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-5
- Rebuilt for Python 3.8

* Tue Aug 20 2019 Susi Lehtola <jussilehtola@fedoraproject.org> - 1.2.3-4
- Rebuilt for GSL 2.6.

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.2.3-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Feb 20 2019 Jerry James <loganjerry@gmail.com> - 1.2.3-1
- New upstream version

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 30 2018 Jerry James <loganjerry@gmail.com> - 1.2.2-1
- New upstream version
- Add -bool patch

* Sat Oct 13 2018 Jerry James <loganjerry@gmail.com> - 1.2.1-1
- New upstream version
- Build with openblas instead of atlas (bz 1619053)
- Drop the python2 subpackage

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.2.0-2
- Rebuilt for Python 3.7

* Sat Jun  2 2018 Jerry James <loganjerry@gmail.com> - 1.2.0-1
- New upstream version

* Tue Mar 20 2018 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1.1.9-8
- Switch examples over to python3

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Jerry James <loganjerry@gmail.com> - 1.1.9-4
- Rebuild for glpk 4.61

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 1.1.9-2
- Rebuild for Python 3.6

* Wed Nov 30 2016 Jerry James <loganjerry@gmail.com> - 1.1.9-1
- New upstream release
- Add a check script

* Mon Sep 26 2016 Dominik Mierzejewski <rpm@greysector.net> - 1.1.8-8
- rebuilt for matplotlib-2.0.0

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-7
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Sat Mar 12 2016 Jerry James <loganjerry@gmail.com> - 1.1.8-6
- Rebuild for glpk 4.59

* Mon Feb 22 2016 Orion Poplawski <orion@cora.nwra.com> - 1.1.8-5
- Rebuild for gsl 2.1

* Fri Feb 19 2016 Jerry James <loganjerry@gmail.com> - 1.1.8-4
- Rebuild for glpk 4.58

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.8-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 1.1.8-2
- Comply with latest python packaging guidelines

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Thu Oct  8 2015 Jerry James <loganjerry@gmail.com> - 1.1.8-1
- New upstream release

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jun 11 2015 Nils Philippsen <nils@redhat.com> - 1.1.7-5
- rebuild for suitesparse-4.4.4

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 1.1.7-4
- Note bundled jquery

* Wed Sep 10 2014 Jerry James <loganjerry@gmail.com> - 1.1.7-3
- Rebuild for suitesparse 4.3.1
- Use a better test for lib64
- Fix license handling

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Tue Jun 17 2014 Jerry James <loganjerry@gmail.com> - 1.1.7-1
- New upstream release
- Drop upstreamed -fixglpkinclude and -glpk patches
- Use better URL for Source0
- Build documentation with python3
- Minor spec file cleanups

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Bohuslav Kabrda <bkabrda@redhat.com> - 1.1.6-5
- Rebuilt for https://fedoraproject.org/wiki/Changes/Python_3.4

* Fri Dec 06 2013 Nils Philippsen <nils@redhat.com> - 1.1.6-4
- rebuild (suitesparse)

* Mon Sep 23 2013 Jerry James <loganjerry@gmail.com> - 1.1.6-3
- Rebuild for atlas 3.10.1

* Tue Jul 30 2013 Jerry James <loganjerry@gmail.com> - 1.1.6-2
- New glpk drops obsolete API; add -glpk patch to move to new API
- Fix Source0 URL

* Tue May 28 2013 Jerry James <loganjerry@gmail.com> - 1.1.6-1
- New upstream release
- New project URL

* Sat Feb  2 2013 Jerry James <loganjerry@gmail.com> - 1.1.5-7
- Rebuild for new glpk

* Sat Nov 17 2012 Jerry James <loganjerry@gmail.com> - 1.1.5-6
- Rebuild for new suitesparse
- Update BRs for texlive 2012

* Wed Oct 10 2012 Jerry James <loganjerry@gmail.com> - 1.1.5-5
- Add linkage to fix undefined symbols (bz 832475)

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 1.1.5-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Tue Apr  3 2012 Jerry James <loganjerry@gmail.com> - 1.1.5-2
- Fix filtering of provides

* Mon Apr  2 2012 Jerry James <loganjerry@gmail.com> - 1.1.5-1
- New upstream release
- Build python3 subpackage

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 1.1.4-2
- Mass rebuild for Fedora 17
- Fix insufficiently escaped filter expression

* Mon Jan  2 2012 Jerry James <loganjerry@gmail.com> - 1.1.4-1
- New upstream release
- Use the RPM 4.9 way of filtering provides

* Wed Jun 22 2011 Jerry James <loganjerry@gmail.com> - 1.1.3-2
- Rebuild due to bz 712251
- Enable the DSDP extension

* Thu May 19 2011 Jerry James <loganjerry@gmail.com> - 1.1.3-1
- New upstream release (bz 700288)
- Ensure linking against ATLAS BLAS instead of system BLAS
- Eliminate unnecessary linkage
- BR python-sphinx and tex4ht for the documentation
- Filter provides from python .so files
- Examples also need pygobject2
- Build documentation in %%build instead of %%prep
- Remove unnecessary elements of the spec file (%%clean, BuildRoot, etc.)

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 30 2010 Orcan Ogetbil <oget[dot]fedora[at[gmail[dot]com> - 1.1-10
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Fri Jul 23 2010 Conrad Meyer <konrad@tylerc.org> - 1.1-9
- Fix glpk include.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 1.1-8
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Conrad Meyer <konrad@tylerc.org> - 1.1-6
- Make examples subpackage noarch.

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Dec 8 2008 Conrad Meyer <konrad@tylerc.org> - 1.1-4
- Add BR on suitesparse-devel.
- Migrate examples to subpackage.

* Mon Dec 8 2008 Conrad Meyer <konrad@tylerc.org> - 1.1-3
- Remove SuiteSparse (copy of system library).

* Mon Dec 8 2008 Conrad Meyer <konrad@tylerc.org> - 1.1-2
- Move examples to datadir/name.
- Include html documentation.
- Package as a proper python egg.

* Mon Dec 8 2008 Conrad Meyer <konrad@tylerc.org> - 1.1-1
- Bump to 1.1.

* Mon Oct 13 2008 Conrad Meyer <konrad@tylerc.org> - 1.0-1
- Initial package.

%{?python_enable_dependency_generator}

%global pkgname Theano
%global srcname theano
%global commit  29d4caa168eaa213cb0b29fd2cb2bef8cd99b389
#%%global rctag a1

Name:           python-theano
Version:        1.0.4
Release:        6%{?rctag:.%{rctag}}%{?dist}.1
Summary:        Mathematical expressions involving multidimensional arrays

License:        BSD
URL:            http://deeplearning.net/software/theano/
Source0:        https://github.com/Theano/Theano/archive/rel-%{version}%{?rctag:%{rctag}}/%{pkgname}-%{version}%{?rctag:%{rctag}}.tar.gz

# Fix the blas interface; see https://github.com/Theano/Theano/issues/6518
Patch0:         %{name}-blas.patch
# Adapt to sphinx 3
Patch2:         %{name}-sphinx3.patch
# Fix FutureWarnings from numpy.  Upstream commits:
# - bb2daf9755c2b05eb9726ca9f52dc6ec487d0129
# - 93e8180bf08b6fbe587b6f0ecc877ec90e6e1681
# Upstream pull requests:
# - https://github.com/Theano/Theano/pull/6711
Patch3:         %{name}-future-warning.patch
# Fix a GammaQ typo.  Upstream pull request:
# - https://github.com/Theano/Theano/pull/6683
Patch4:         %{name}-gammaq.patch
# Adapt to new ceil, floor, and trunc handling in numpy 1.17.0
Patch5:         %{name}-ceil-floor-trunc.patch
# A test that involves tracebacks has an extra frame with numpy 1.17.0
Patch6:         %{name}-traceback.patch
# The behavior of numpy.clip changed in 1.17.0.  One test checks whether the
# theano clip implementation matches the behavior of numpy.clip.  That test is
# doomed to failure with numpy 1.17.0, so just remove it.
Patch7:         %{name}-clip.patch
# Tests that used to fail with ValueError no longer do with numpy 1.17.0
Patch8:         %{name}-random.patch
# Tests that used to fail with numpy 1.17.0 with TypeError: only integer scalar
# arrays can be converted to a scalar index
Patch9:         %{name}-sort.patch
# More robustly import Iterable.  Upstream commits:
# - https://github.com/Theano/Theano/commit/513c676ae3ddcae6d23a7e62db19884eaa8c1008
# - https://github.com/Theano/Theano/commit/454f4e56c4a859d2f3b48592c731464bf78df342
# - https://github.com/Theano/Theano/commit/11bd36d580c6ea2a67f9b2fa1483670f63a6a13b
Patch10:        %{name}-iterable.patch
# Do not try to invoke git to find the commit
Patch11:        %{name}-git.patch
# Fix some malformed format strings
Patch12:        %{name}-format.patch
# Fix some incorrect uses of the 'is' keyword
Patch13:        %{name}-is.patch
# Fix documentation bugs resulting in sphinx warnings
Patch14:        %{name}-doc.patch
# Scipy 1.3.x produces sorted indices, so do not assert they are unsorted
Patch15:        %{name}-has-sorted-indices.patch
# Fix the import of various classes that have moved across python versions
# https://github.com/Theano/Theano/pull/6741
Patch16:        %{name}-ordered-dict.patch

BuildArch:      noarch

BuildRequires:  gcc-c++
BuildRequires:  gcc-gfortran
BuildRequires:  git-core
BuildRequires:  openblas-devel
BuildRequires:  tex(latex)
BuildRequires:  tex(anyfontsize.sty)
BuildRequires:  tex-dvipng

BuildRequires:  python3-devel
BuildRequires:  python3-pygpu-devel
BuildRequires:  python3dist(cython)
BuildRequires:  python3dist(nose)
BuildRequires:  python3dist(numpy)
BuildRequires:  python3dist(parameterized)
BuildRequires:  python3dist(pygments)
BuildRequires:  python3dist(scipy)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-rtd-theme)

%global _desc %{expand:
Theano is a Python library that allows you to define, optimize, and
evaluate mathematical expressions involving multi-dimensional arrays
efficiently.  Theano features:
- tight integration with NumPy: Use numpy.ndarray in Theano-compiled
  functions.
- transparent use of a GPU: Perform data-intensive calculations up to
  140x faster than with CPU (float32 only).
- efficient symbolic differentiation: Theano does your derivatives for
  function with one or many inputs.
- speed and stability optimizations: Get the right answer for log(1+x)
  even when x is really tiny.
- dynamic C code generation: Evaluate expressions faster.
- extensive unit-testing and self-verification: Detect and diagnose many
  types of mistake.}

%description %_desc

%package -n python3-%{srcname}
Summary:        %{summary}
Requires:       openblas-devel
Requires:       gcc-c++
Requires:       gcc-gfortran
Recommends:     python%{python3_version}dist(pygpu)
Suggests:       python%{python3_version}dist(pydot)

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname} %_desc

%package doc
Summary:        Theano documentation
Requires:       fontawesome-fonts-web
Requires:       font(fontawesome)
Requires:       font(lato)
Requires:       font(robotoslab)

%description doc
User documentation for Theano.

%prep
%autosetup -n %{pkgname}-rel-%{version}%{?rctag:%{rctag}} -p0

# We don't need to use /usr/bin/env
for fil in $(grep -FRl /bin/env .); do
  sed -ri.orig 's,( )?(/usr)?/bin/env[[:blank:]]*python.*,%{_bindir}/python3,' $fil
  touch -r $fil.orig $fil
  rm $fil.orig
done

# We don't have a git checkout, so don't invoke git to find the commit
sed -i 's/@@tag@@/%{commit}/' doc/conf.py

# Remove linter test
rm theano/tests/test_flake8.py

%build
# Regenerate the Cython files, and fix the numpy interfaces
cython -3 -o theano/scan_module/c_code/scan_perform.c \
             theano/scan_module/scan_perform.pyx
sed -e 's/\(__pyx_v_self\)->descr/PyArray_DESCR(\1)/' \
    -e 's/\(__pyx_v_arr\)->base = \(.*\);/PyArray_SetBaseObject(\1, \2);/' \
    -e 's/\(__pyx_v_arr\)->base/PyArray_BASE(\1)/' \
    -i theano/scan_module/c_code/scan_perform.c

%py3_build

# Build the documentation
export PYTHONPATH=$PWD
%{__python3} doc/scripts/docgen.py --nopdf
rst2html --no-datestamp README.rst README.html

# Remove build artifacts
rm -fr html/.buildinfo html/.doctrees

# Do not bundle fonts into the documentation
cd html/_static/fonts
for suffix in eot svg ttf woff woff2; do
  rm fontawesome-webfont.$suffix
  ln -s %{_datadir}/fonts/fontawesome/fontawesome-webfont.$suffix .
done
rm {Lato,RobotoSlab}/*.ttf
ln -s %{_datadir}/fonts/lato/Lato-Bold.ttf Lato/lato-bold.ttf
ln -s %{_datadir}/fonts/lato/Lato-BoldItalic.ttf Lato/lato-bolditalic.ttf
ln -s %{_datadir}/fonts/lato/Lato-Italic.ttf Lato/lato-italic.ttf
ln -s %{_datadir}/fonts/lato/Lato-Regular.ttf Lato/lato-regular.ttf
ln -s %{_datadir}/fonts/google-roboto-slab/RobotoSlab-Bold.ttf RobotoSlab/roboto-slab-v7-bold.ttf
ln -s %{_datadir}/fonts/google-roboto-slab/RobotoSlab-Regular.ttf RobotoSlab/roboto-slab-v7-regular.ttf
cd -

%install
%py3_install

# Restore executable permission on the scripts
chmod a+x $(find %{buildroot} -name \*.py -o -name \*.sh | xargs grep -l '^#!')

%check
%ifarch %{power64}
# FIXME: some tests fail on ppc64le
# The conv3d2d tests compute the wrong type of values (float32 instead of
# float64) and the wrong values.
sed -i '/parameterized\.expand/,$d' ttheano/tensor/nnet/tests/test_conv3d2d.py

# An unexpected GradientError is thrown at theano/gradient.py line 1790
rm theano/tensor/nnet/tests/test_corr3d.py
%endif

%{__python3} bin/theano-nose --processes=0 --process-restartworker

%files -n python3-%{srcname}
%doc DESCRIPTION.txt HISTORY.txt NEWS.txt README.html
%license doc/LICENSE.txt
%{_bindir}/theano-*
%{python3_sitelib}/Theano-*.egg-info/
%{python3_sitelib}/theano/
%{python3_sitelib}/bin/

%files doc
%doc html

%changelog
* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-6.1
- Rebuilt for Python 3.9

* Tue Feb  4 2020 Jerry James <loganjerry@gmail.com> - 1.0.4-6
- Add -ordered-dict patch, thanks to Miro Hrončok (bz 1797982)

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-5.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Mon Nov 25 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-5
- Drop epydoc BR since it has been retired
- Unbundle fonts from the documentation
- Ship an HTML form of the README
- Add -has-sorted-indices patch

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-4.1
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Thu Aug 29 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-4
- Add -iterable, -git, -format, -is, and -doc patches to fix warnings

* Fri Aug 23 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.0.4-3
- Fix FTBFS with python-theano-sort patch (#1737011)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 1.0.4-2.1
- Rebuilt for Python 3.8

* Fri Aug 16 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-2
- Add -future-warning, -gammaq, -ceil-floor-trunc, -traceback, -clip, and
  -random patches to fix FTBFS (bz 1737011)

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.4-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jan 19 2019 Jerry James <loganjerry@gmail.com> - 1.0.4-1
- New upstream release

* Thu Dec 27 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.3-2
- Drop duplicated dependencies

* Sat Oct  6 2018 Jerry James <loganjerry@gmail.com> - 1.0.3-1
- New upstream release
- Partially revert the previous commit; the gcc Requires is needed
- Build with openblas instead of atlas
- Send cython output to the correct directory
- Build with pygpu support

* Sun Aug 12 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.2-2
- Drop python2 subpackage

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.2-1.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 1.0.2-1.1
- Rebuilt for Python 3.7

* Wed May 23 2018 Jerry James <loganjerry@gmail.com> - 1.0.2-1
- New upstream release

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 22 2017 Jerry James <loganjerry@gmail.com> - 1.0.1-1
- New upstream release
- Add -blas patch to fix compilation errors when using the blas interface
- Reenable the tests
- Pass nose flags to prevent memory exhaustion while running the tests

* Fri Nov 17 2017 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.0.0-1
- Update to 1.0.0

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Mar 22 2017 Jerry James <loganjerry@gmail.com> - 0.9.0-1
- New upstream release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-1.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.8.2-1.2
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.2-1.1
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Apr 21 2016 Jerry James <loganjerry@gmail.com> - 0.8.2-1
- New upstream release

* Fri Apr 15 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-2
- Remove python2 dependency from the python3 subpackage (bz 1324232)
- Recommend pydot instead of requiring it

* Sat Apr  2 2016 Jerry James <loganjerry@gmail.com> - 0.8.1-1
- New upstream release
- Fix the pydot dependencies

* Wed Mar 23 2016 Jerry James <loganjerry@gmail.com> - 0.8.0-1
- New upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-0.2.a1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Feb  1 2016 Jerry James <loganjerry@gmail.com> - 0.7.1-0.1.a1
- Comply with latest python packaging guidelines

* Thu Nov 12 2015 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 0.7.1-0.1.a1
- Update to 0.7.1a1

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-2.2
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Wed Nov  4 2015 Toshio Kuratomi <toshio@fedoraproject.org> - 0.7.0-2.1
- Fix python3 package requiring python2.

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.7.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Wed Apr  1 2015 Jerry James <loganjerry@gmail.com> - 0.7.0-1
- New upstream release
- Drop upstreamed -arm patch
- Regenerate cython files to fix build failure

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.6.0-5
- Add -arm patch to fix build failure on arm builders due to inverted test

* Sat Feb 21 2015 Jerry James <loganjerry@gmail.com> - 0.6.0-4
- Drop workaround for fixed bug (bz 1075826)
- Use license macro

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed May 14 2014 Jerry James <loganjerry@gmail.com> - 0.6.0-3
- Rebuild for https://fedoraproject.org/wiki/Changes/Python_3.4

* Thu Mar 13 2014 Jerry James <loganjerry@gmail.com> - 0.6.0-2
- Add python3 subpackage
- Add another icon to the -missing tarball
- Update source icons
- Unbundle python-six
- Add workaround for bz 1075826

* Sat Dec  7 2013 Jerry James <loganjerry@gmail.com> - 0.6.0-1
- New upstream release
- Drop upstreamed -import patch

* Mon Oct 21 2013 Jerry James <loganjerry@gmail.com> - 0.6.0-0.1.rc3
- Add the -import patch to fix an exception
- Add more files to the base package docs

* Tue Aug 27 2013 Jerry James <loganjerry@gmail.com> - 0.6.0-0.rc3
- Initial RPM

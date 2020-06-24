Name:           python3-mypy
Version:        0.782
Release:        1%{?dist}
Summary:        A static type checker for Python
%{?python_provide:%python_provide python3-mypy}

# The files under lib-python and lib-typing/3.2 are Python-licensed, but this
# package does not include those files
# mypy/typeshed is ASL 2.0
License:        MIT and ASL 2.0
URL:            https://github.com/python/mypy
Source0:        https://github.com/python/mypy/archive/v%{version}/mypy-%{version}.tar.gz

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python-typeshed
BuildRequires:  python3-typing-extensions
Requires:  python-typeshed
Requires:  python3-typing-extensions

# Needed to generate the man pages
BuildRequires:  help2man
BuildRequires:  (python3dist(typed-ast) >= 1.4 with python3dist(typed-ast) < 1.5)
BuildRequires:  (python3dist(mypy-extensions) >= 0.4 with python3dist(mypy-extensions) < 0.5)

BuildArch:      noarch

%description
Mypy is an optional static type checker for Python.  You can add type
hints to your Python programs using the upcoming standard for type
annotations introduced in Python 3.5 beta 1 (PEP 484), and use mypy to
type check them statically. Find bugs in your programs without even
running them!

%prep
%autosetup -n mypy-%{version} -p1
rm -vrf *.egg-info/

%build
%py3_build

%install
%py3_install
rm -vrf %{buildroot}%{python3_sitelib}/mypy/{test,typeshed/tests}
ln -s /usr/share/typeshed %{buildroot}%{python3_sitelib}/mypy/typeshed

# Generate man pages
mkdir -p %{buildroot}%{_mandir}/man1
PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/mypy.1 \
        %{buildroot}%{_bindir}/mypy

PYTHONPATH=%{buildroot}%{python3_sitelib} \
    help2man --no-info --version-string 'mypy stubgen %{version}-dev' \
        --no-discard-stderr -o %{buildroot}%{_mandir}/man1/stubgen.1 \
        %{buildroot}%{_bindir}/stubgen

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/mypy
%{python3_sitelib}/mypy-*.egg-info
%{python3_sitelib}/mypyc
%{_bindir}/mypy
%{_bindir}/mypyc
%{_bindir}/dmypy
%{_bindir}/stubgen
%{_bindir}/stubtest
%{_mandir}/man1/mypy.1*
%{_mandir}/man1/stubgen.1*

%changelog
* Tue Jun 23 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.782-1
- 0.782

* Fri Jun 19 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.781-1
- 0.781

* Fri Jun 05 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.780-1
- 0.780

* Tue May 26 2020 Miro Hrončok <mhroncok@redhat.com> - 0.770-2
- Rebuilt for Python 3.9

* Tue Mar 10 2020 Gwyn Ciesla <gwync@protonmail.com> - 0.770-1
- 0.770

* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.761-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Dec 20 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.761-1
- 0.761

* Wed Dec 18 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.760-1
- 0.760

* Mon Dec 02 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.750-1
- 0.750

* Mon Nov 11 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.740-2
- Require/BR python3-typing-extensions

* Thu Oct 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.740-1
- 0.740

* Tue Oct 08 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.730-2
- Fix typeshed.

* Thu Sep 26 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.730-1
- 0.730

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 0.720-3
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.720-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.720-1
- 0.720

* Mon Jun 24 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.711-1
- 0.711

* Wed Jun 19 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.710-1
- 0.710

* Wed Apr 17 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.701-1
- 0.701

* Wed Apr 03 2019 Gwyn Ciesla <gwync@protonmail.com> - 0.700-1
- Update to 0.700

* Sat Feb 23 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.670-1
- Update to 0.670

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.620-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Sep 25 2018 Matus Honek <mhonek@redhat.com> - 0.620-2
- Add BuildRequire to fix man page generation

* Fri Aug 10 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.620-1
- 0.620

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.600-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 0.600-2
- Rebuilt for Python 3.7

* Tue May 08 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.600-1
- 0.600

* Tue Mar 27 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.580-1
- 0.580

* Mon Mar 05 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.570-1
- 0.570

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.560-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Jan 22 2018 Gwyn Ciesla <limburgher@gmail.com> - 0.560-2
- python3-psutil requires.

* Mon Dec 18 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.560-1
- 0.560

* Mon Nov 13 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.550-1
- 0.550

* Mon Oct 23 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.540-1
- 0.540

* Fri Oct 20 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.530-1
- 0.530

* Tue Sep 05 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.521-3
- Typeshed patch.

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.521-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Tue Jul 25 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.521-1
- 0.521

* Tue Jul 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.520-1
- 0.520

* Sun Jun 11 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.511-2
- Add python3-typed_ast Requires.

* Fri Jun 09 2017 Gwyn Ciesla <limburgher@gmail.com> - 0.511-1
- New upstream.

* Sat May 13 2017 Stephen Gallagher <sgallagh@redhat.com> - 0.4.6-4
- Add dist tag back to Release

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.4.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.4.6-2
- Rebuild for Python 3.6

* Mon Dec 19 2016 CAI Qian <caiqian@redhat.com> - 0.4.6-1
- Update to mypy 0.4.6

* Tue Dec 13 2016 Stratakis Charalampos <cstratak@redhat.com> - 0.4.3-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.3-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Mon Jul 18 2016 David Shea <dshea@redhat.com> - 0.4.3-1
- Update to mypy 0.4.3

* Mon Jun 13 2016 David Shea <dshea@redhat.com> - 0.4.2-1
- Update to mypy 0.4.2

* Thu May 19 2016 David Shea <dshea@redhat.com> - 0.4.1-2
- Fix build issues

* Tue May 17 2016 David Shea <dshea@redhat.com> - 0.4.1-1
- Update to mypy 0.4.1

* Mon Feb 22 2016 David Shea <dshea@redhat.com> - 0.3.1-1
- Update to the first post-3.5 actual upstream release

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.2.0-2.dev20160128git
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 28 2016 David Shea <dshea@redhat.com> - 0.2.0-1.dev20160128git
- Generalize yield statement function type
- Avoid crash on outrageous non-ASCII characters.
- No longer need to pin flake8 version.
- Find partial types anywhere in the stack. (removes local patch)
- Update license year range to 2016
- If a base class is Any, don't get default constructor signature from object.
- Simplify union types when determining type sameness
- Generator fixup
- Add line number to "__init__ must return None" error
- Fix empty yield error in unannotated functions
- Fix "except (E1, E2):" parsing in PY2.
- Don't crash if no source files were found in a directory or package.
- Fail without traceback when duplicate module name encountered.
- Fix subtype check between generic class and Callable
- Avoid crash on "x in y" where y has a partial type.
- Fix type inference issue with dict(x=[], y=[])
- Fix #1160 (bogus error message)
- Fix function definition within for statement

* Fri Jan 15 2016 David Shea <dshea@redhat.com> - 0.2.0-1.dev20160115git
- Fix the order in which builtins are loaded.
- Fix crash on undefined variable actual_types in check_argument_count (replaces local patch)
- Fixes for Generator support
- Fix crash in check_overlapping_op_methods
- Hopeful fix for #1002 (lxml trouble)
- No longer need to pin flake8 version.
- Find partial types anywhere in the stack. (not yet committed upstream)

* Mon Jan 11 2016 David Shea <dshea@redhat.com> - 0.2.0-1.dev20160111git
- Add support for more kinds of function redefinition
- Allow conditionally assigning None to a module
- Support conditionally defined nested functions
- Tighten argument type for Instance(erased=...) from Any to bool.
- Reformat a few messages so they are easier to find using grep.
- Update README.md to fix installation instructions for Python 3.5

* Thu Jan  7 2016 David Shea <dshea@redhat.com> - 0.2.0-1.dev20160104git.1
- Fix a bug in the discovery of the typeshed files

* Mon Jan  4 2016 David Shea <dshea@redhat.com> - 0.2.0-1.dev20160104git
- Don't check git submodule in subprocesses.
- Improve check for "# type: ignore".
- Add --pdb flag to drop into pdb upon fatal error.
- Don't report internal error when using a name that could not be imported.
- Write type-checking errors to stdout. Make usage() more complete.
- Avoid ever relying on a not-yet-initialized MRO
- When comparing template to actual arg types, stop at shortest.
- Be more clever about finding a Python 2 interpreter
- Basic support for partial 'None' types
- Handle multiple None initializers
- Remove redundant annotations
- Partial type improvements
- Allow assignments to function definitions
- Document --pdb option.
- Look for the keyword type in the right place.

* Mon Dec 21 2015 David Shea <dshea@redhat.com> - 0.2.0-1.dev20151220git
- Fix an internal error when updating a partial type from an outer scope

* Thu Dec 17 2015 David Shea <dshea@redhat.com> - 0.2.0-1.dev20151217git
- Initial package

# !!! WARNING !!!
# This package has very fragile tests. If they fail, build it again couple
# times before filling bugz.

Name:           pipenv 
Version:        2018.11.26
Release:        13%{?dist}
Summary:        The higher level Python packaging tool

# Pipenv source code is MIT, there are bundled packages having different licenses

# pipenv/patched/crayons.py is MIT
# pipenv/patched/pipfile/ is (ASL 2.0 or BSD)
# pipenv/patched/piptools/ is BSD
# pipenv/patched/safety/ is MIT
# pipenv/patched/safety.zip is MIT

# pipenv/patched/notpip/ is MIT
# pipenv/patched/notpip/_vendor/appdirs.py is MIT
# pipenv/patched/notpip/_vendor/backports/enum/ is BSD
# pipenv/patched/notpip/_vendor/backports/functools_lru_cache.py is MIT
# pipenv/patched/notpip/_vendor/backports/shutil_get_terminal_size/ is MIT
# pipenv/patched/notpip/_vendor/backports/weakref.py is Python
# pipenv/patched/notpip/_vendor/cachecontrol/ is ASL 2.0
# pipenv/patched/notpip/_vendor/certifi/ is MPLv2.0
# pipenv/patched/notpip/_vendor/chardet/ is LGPLv2+
# pipenv/patched/notpip/_vendor/colorama/ is BSD
# pipenv/patched/notpip/_vendor/distlib/ is Python
# pipenv/patched/notpip/_vendor/distro.py is ASL 2.0
# pipenv/patched/notpip/_vendor/html5lib/ is MIT
# pipenv/patched/notpip/_vendor/idna/ is Python
# pipenv/patched/notpip/_vendor/ipaddress.py is Python
# pipenv/patched/notpip/_vendor/lockfile/ is Python
# pipenv/patched/notpip/_vendor/msgpack/ is ASL 2.0
# pipenv/patched/notpip/_vendor/packaging/ is (ASL 2.0 or BSD)
# pipenv/patched/notpip/_vendor/pathlib2/ is MIT
# pipenv/patched/notpip/_vendor/pep517/ is MIT
# pipenv/patched/notpip/_vendor/pkg_resources/ is MIT 
# pipenv/patched/notpip/_vendor/progress/ is ISC
# pipenv/patched/notpip/_vendor/pyparsing.py is MIT
# pipenv/patched/notpip/_vendor/pytoml/ is MIT
# pipenv/patched/notpip/_vendor/requests/ is ASL 2.0
# pipenv/patched/notpip/_vendor/retrying.py is ASL 2.0
# pipenv/patched/notpip/_vendor/scandir.py is BSD
# pipenv/patched/notpip/_vendor/six.py is ASL 2.0
# pipenv/patched/notpip/_vendor/urllib3/ is MIT
# pipenv/patched/notpip/_vendor/webencodings/ is ASL 2.0

# pipenv/vendor/click_didyoumean/ is MIT
# pipenv/vendor/click_completion/ is MIT
# pipenv/vendor/cursor is CC-BY-SA
# pipenv/vendor/delegator.py is MIT
# pipenv/vendor/passa is ISC
# pipenv/vendor/requirementslib/ is (Apache2.0 or BSD)
# pipenv/vendor/resolvelib/ is MIT
# pipenv/vendor/shutilwhich/ is BSD
# pipenv/vendor/tomlkit/ is MIT

License:        MIT and BSD and ASL 2.0 and LGPLv2+ and Python and ISC and MPLv2.0 and (ASL 2.0 or BSD) and CC-BY-SA
URL:            https://github.com/pypa/pipenv
Source0:        https://github.com/pypa/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz

# Adds "pytest_pypi.plugin import pypi, ..." to conftest,
# as we don't have that plugin installed and it is not autodiscovered
Patch2:         0002-import-pytest-pypi.patch

# A couple of tests fails in the mock environment, add option
# to skip these using special pytest marker
# TODO fix and propose changes upstream
Patch3:         0003-rpmfail-pytest-marker.patch

# Use the system level root certificate instead of the one bundled in certifi
# https://bugzilla.redhat.com/show_bug.cgi?id=1655253
Patch4:         dummy-certifi.patch

BuildArch:      noarch

BuildRequires:  ca-certificates
# gcc is only needed for tests, this is a noarch package
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  python3-devel
BuildRequires:  python3dist(flaky)
BuildRequires:  python3dist(flask)
BuildRequires:  python3dist(mock)
BuildRequires:  python3dist(parver)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(pytest-xdist)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx-click)
BuildRequires:  python3dist(twine)
BuildRequires:  python3dist(virtualenv)
BuildRequires:  python3dist(virtualenv-clone)

# Optional condition that makes "python" mean Python 2
# Useful to tests if pipenv can manage python 2 venvs, but unnecessary dep
%bcond_with python2_tests

%if %{with python2_tests}
BuildRequires:  python2-devel
%endif

# Packages vendored upstream
BuildRequires:  python3dist(appdirs)
BuildRequires:  python3dist(attrs)
BuildRequires:  python3dist(blindspin) >= 2.0.1
BuildRequires:  python3dist(cached-property) >= 1.3
BuildRequires:  python3dist(cerberus) >= 1.2
BuildRequires:  python3dist(certifi)
BuildRequires:  python3dist(click) >= 7
BuildRequires:  python3dist(colorama) >= 0.3.9
BuildRequires:  python3dist(distlib) >= 0.2.7
BuildRequires:  python3dist(docopt) >= 0.6.2
BuildRequires:  python3dist(first) >= 2.0.1
BuildRequires:  python3dist(chardet) >= 2.0.1
BuildRequires:  python3dist(iso8601) >= 0.1.11
BuildRequires:  python3dist(jinja2) >= 2.10
BuildRequires:  python3dist(markupsafe) >= 1
BuildRequires:  python3dist(packaging) >= 17.1
BuildRequires:  python3dist(parse) >= 1.8.4
BuildRequires:  python3dist(pexpect) >= 4.6
BuildRequires:  python3dist(ptyprocess) >= 0.6
BuildRequires:  python3dist(pyparsing) >= 2.2
BuildRequires:  python3dist(python-dotenv) >= 0.9.1
BuildRequires:  python3dist(requests) >= 2.20
BuildRequires:  python3dist(semver) >= 2.8.1
BuildRequires:  python3dist(shellingham) >= 1.2.7
BuildRequires:  python3dist(six)
BuildRequires:  python3dist(toml) >= 0.10
BuildRequires:  python3dist(urllib3)
BuildRequires:  python3dist(yarg) >= 0.1.9
BuildRequires:  python3dist(yaspin)
BuildRequires:  python3dist(vistir)
BuildRequires:  python3dist(pipdeptree)
BuildRequires:  python3dist(pipreqs)
BuildRequires:  python3dist(pip-shims)
BuildRequires:  python3dist(plette)
BuildRequires:  python3dist(pythonfinder)

%{?python_provide:%python_provide python3-%{name}}

Requires:       ca-certificates
Requires:       which

Requires:       python3dist(virtualenv-clone)
Requires:       python3dist(virtualenv)

# Packages vendored upstream
Requires:       python3dist(appdirs)
Requires:       python3dist(attrs)
Requires:       python3dist(blindspin) >= 2.0.1
Requires:       python3dist(cached-property) >= 1.3
Requires:       python3dist(cerberus) >= 1.2
Requires:       python3dist(certifi)
Requires:       python3dist(click) >= 7
Requires:       python3dist(colorama) >= 0.3.9
Requires:       python3dist(distlib) >= 0.2.7
Requires:       python3dist(docopt) >= 0.6.2
Requires:       python3dist(first) >= 2.0.1
Requires:       python3dist(chardet) >= 2.0.1
Requires:       python3dist(iso8601) >= 0.1.11
Requires:       python3dist(jinja2) >= 2.10
Requires:       python3dist(markupsafe) >= 1
Requires:       python3dist(packaging) >= 17.1
Requires:       python3dist(parse) >= 1.8.4
Requires:       python3dist(pexpect) >= 4.6
Requires:       python3dist(ptyprocess) >= 0.6
Requires:       python3dist(pyparsing) >= 2.2
Requires:       python3dist(python-dotenv) >= 0.9.1
Requires:       python3dist(requests) >= 2.20
Requires:       python3dist(semver) >= 2.8.1
Requires:       python3dist(shellingham) >= 1.2.7
Requires:       python3dist(six)
Requires:       python3dist(toml) >= 0.10
Requires:       python3dist(urllib3)
Requires:       python3dist(yarg) >= 0.1.9
Requires:       python3dist(yaspin)
Requires:       python3dist(vistir)
Requires:       python3dist(pipdeptree)
Requires:       python3dist(pipreqs)
Requires:       python3dist(pip-shims)
Requires:       python3dist(plette)
Requires:       python3dist(pythonfinder)

# Following packages bundled under vendor directory are not
# packaged for Fedora yet.
# TODO package for Fedora and unbundle
Provides:       bundled(python3dist(click-didyoumean)) == 0.0.3
Provides:       bundled(python3dist(delegator.py)) == 0.1.1
# Needs requirementslib (see below)
Provides:       bundled(python3dist(passa))
# This library uses pip.internals. Some changes in init methods happened there.
# So version 1.3.3 is useless with pip 19+ and newer versions will break pipenv
# because pipenv has bundled patched pip.
Provides:       bundled(python3dist(requirementslib)) == 1.3.3
# Dependency of passa
Provides:       bundled(python3dist(resolvelib)) == 0.2.2

# No longer used in upstream master branch, not worth looking into
Provides:       bundled(python3dist(shutilwhich)) == 1.1
Provides:       bundled(python3dist(cursor)) == 1.2

# The sources contains patched versions of following packages:
Provides:       bundled(python3dist(crayons)) == 0.1.2
Provides:       bundled(python3dist(pipfile)) == 0.0.2
Provides:       bundled(python3dist(pip-tools)) == 3.1
Provides:       bundled(python3dist(pip)) == 18.1
Provides:       bundled(python3dist(safety))

# We cannot unbundle this easily,
# See https://bugzilla.redhat.com/show_bug.cgi?id=1767003
Provides:       bundled(python3dist(backports.functools_lru_cache)) == 1.5
Provides:       bundled(python3dist(backports.shutil_get_terminal_size)) == 1.0.0
Provides:       bundled(python3dist(backports.shutil_get_terminal_size)) == 1.0.0
Provides:       bundled(python3dist(click-completion)) == 0.5.0
Provides:       bundled(python3dist(enum34)) == 1.1.6
Provides:       bundled(python3dist(pathlib2)) == 2.3.2
Provides:       bundled(python3dist(scandir)) == 1.9
Provides:       bundled(python3dist(tomlkit)) == 0.5.2

# The packages bundled with pip (18.1):
Provides:       bundled(python3dist(appdirs)) = 1.4.3
Provides:       bundled(python3dist(distlib)) = 0.2.7
Provides:       bundled(python3dist(distro)) = 1.3
Provides:       bundled(python3dist(html5lib)) = 1.0.1
Provides:       bundled(python3dist(six)) = 1.11
Provides:       bundled(python3dist(colorama)) = 0.3.9
Provides:       bundled(python3dist(CacheControl)) = 0.12.5
Provides:       bundled(python3dist(msgpack-python)) = 0.5.6
Provides:       bundled(python3dist(lockfile)) = 0.12.2
Provides:       bundled(python3dist(progress)) = 1.4
Provides:       bundled(python3dist(ipaddress)) = 1.0.22
Provides:       bundled(python3dist(packaging)) = 18
Provides:       bundled(python3dist(pep517)) = 0.2
Provides:       bundled(python3dist(pyparsing)) = 2.2.1
Provides:       bundled(python3dist(pytoml)) = 0.1.19
Provides:       bundled(python3dist(retrying)) = 1.3.3
Provides:       bundled(python3dist(requests)) = 2.19.1
Provides:       bundled(python3dist(chardet)) = 3.0.4
Provides:       bundled(python3dist(idna)) = 2.7
Provides:       bundled(python3dist(urllib3)) = 1.23
Provides:       bundled(python3dist(certifi)) = 2018.8.24
Provides:       bundled(python3dist(setuptools)) = 40.4.3
Provides:       bundled(python3dist(webencodings)) = 0.5.1

%description
The officially recommended Python packaging tool that aims to bring
the best of all packaging worlds (bundler, composer, npm, cargo, yarn, etc.)
to the Python world. It automatically creates and manages a virtualenv for 
your projects, as well as adds/removes packages from your Pipfile as you 
install/uninstall packages. It also generates the ever–important Pipfile.lock, 
which is used to produce deterministic builds.

%package -n %{name}-doc
Summary:        Pipenv documentation
%description -n %{name}-doc
Documentation for Pipenv


%prep
%autosetup -p1 -n %{name}-%{version}

# https://github.com/pypa/pipenv/issues/3326
sed -i 's/2018.11.15.dev0/%{version}/' pipenv/__version__.py

# this goes together with patch4
rm pipenv/patched/notpip/_vendor/certifi/*.pem

# Remove packages that are already packaged for Fedora from vendor directory
UNBUNDLED="appdirs attr blindspin cached_property cerberus click colorama distlib docopt first chardet iso8601 jinja2 markupsafe packaging parse pexpect ptyprocess pyparsing dotenv requests certifi idna urllib3 semver shellingham six toml yarg yaspin vistir pythonfinder plette pipreqs pipdeptree pip_shims"

# issue: for loop below doesn't handle multiple imports in one line
# properly. There might be case when library is still not unbundled
# but is not imported from vendor directory.
# diff of pyenv.py:
#  265   │ -from .vendor import attr, delegator
#  266   │ +import attr, delegator
# So we unpack such import statements into multiple lines first:
while matches=$(grep -Elr 'from (\.pipenv)?\.vendor import ([^,]+), (.+)'); do
  sed -Ei 's/from (\.pipenv)?\.vendor import ([^,]+), (.+)/from \1.vendor import \2\nfrom \1.vendor import \3/g' $matches
done

for pkg in ${UNBUNDLED[@]}; do
  find pipenv/* tests/* -not -path '*/\.git*' -type f -exec sed -i -E \
  -e "s/from (pipenv)?\.vendor\.${pkg}(\.\S+)? import/from ${pkg}\2 import/" \
  -e "s/^import (pipenv)?\.vendor\.${pkg}(\.\S+)?/import ${pkg}\2/" \
  -e "s/from (pipenv)?\.vendor import ${pkg}(\.\S+)?/import ${pkg}\2/" \
  -e "s/(pipenv)?\.vendor\.${pkg}(\.\S+)?/${pkg}\2/g" {} \;
done

_vendordir="pipenv/vendor/"

for pkg in ${UNBUNDLED[@]}; do
  if [ -d $_vendordir$pkg ]; then
    rm -r $_vendordir$pkg
  elif [ -f $_vendordir$pkg.py ]; then
    rm $_vendordir$pkg".py"
  else
    echo 'Unbundling error:' $pkg 1>&2
    exit 1
  fi
  rm -rf $_vendordir$pkg".LICENSE"*
  rm -rf $_vendordir${pkg/_/-}".LICENSE"*

  if grep -rE "( |\.)vendor\.$pkg" pipenv; then
    echo 'Unbundling error:' $pkg 1>&2
    exit 1
  fi
done

# Remove setup_requires, as we cannot install invoke
sed -i /setup_requires/d setup.py

# Hotfix for pytest 4
# https://github.com/pypa/pipenv/pull/3724
sed -i 's/get_marker/get_closest_marker/g' tests/integration/conftest.py


%build
%py3_build
# generate html docs
export PYTHONPATH=$PWD/build/lib
sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
rm -rf html/_sources/

%install
%py3_install
# Remove shebang lines from scripts in project directory
grep "/usr/bin/env python" -lR %{buildroot}%{python3_sitelib}/%{name}| xargs sed -i '1d'

%check
# dirty dirty hack (TODO find a better way)
# for the tests to run, we need to set PYTHONPATH to something that:
#   - has our pipenv (%%{buildroot}%%{python3_sitelib})
#   - has our unbundled deps (%%{python3_sitelib} and %%{python3_sitearch})
#   - doesn't have pip (venv installed pips may have different API)
#   - doesn't have requests (a test uninstalls it and checks it)
# (even externally run pythons read PYTHONPATH and use modules from it)
mkdir check_pythonpath
ln -sf %{buildroot}%{python3_sitelib}/* %{python3_sitelib}/* %{python3_sitearch}/* check_pythonpath/
unlink check_pythonpath/pip
unlink check_pythonpath/pip-*info
unlink check_pythonpath/__pycache__
mkdir check_pythonpath/__pycache__
ln -sf %{python3_sitelib}/__pycache__/* %{python3_sitearch}/__pycache__/* check_pythonpath/__pycache__/

# we also make sure "python" exists and means something
mkdir check_path
%if %{with python2_tests}
ln -s %{__python2} check_path/python
%else
ln -s %{__python3} check_path/python
%endif
test -f %{_bindir}/virtualenv || ln -s %{_bindir}/virtualenv-3 check_path/virtualenv

export PATH=$PWD/check_path:$PATH:%{buildroot}%{_bindir}
export PYTHONPATH=$PWD/check_pythonpath:$PWD/tests/pytest-pypi
export PYPI_VENDOR_DIR="$(pwd)/tests/pypi/"
sed -i 's/-n auto//' pytest.ini # disable -n auto for now https://github.com/pytest-dev/pytest-xdist/issues/381
pytest-3 -v -m "not rpmfail" tests

rm -rf check_pythonpath check_path


%files
%license LICENSE
# for the sake of simplicity, files are listed twice. we know about it
%license %{python3_sitelib}/%{name}/patched/crayons.LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/cachecontrol/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/certifi/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/chardet/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/colorama/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/distlib/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/html5lib/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/idna/LICENSE.rst
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/lockfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/msgpack/COPYING
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/packaging/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pep517/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pkg_resources/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/progress/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/pytoml/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/requests/LICENSE
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/urllib3/LICENSE.txt
%license %{python3_sitelib}/%{name}/patched/notpip/_vendor/webencodings/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.APACHE
%license %{python3_sitelib}/%{name}/patched/pipfile/LICENSE.BSD
%license %{python3_sitelib}/%{name}/patched/piptools/LICENSE
%license %{python3_sitelib}/%{name}/patched/safety/LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/enum/LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/functools_lru_cache.LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/shutil_get_terminal_size/LICENSE
%license %{python3_sitelib}/%{name}/vendor/backports/weakref.LICENSE
%license %{python3_sitelib}/%{name}/vendor/click_didyoumean/LICENSE
%license %{python3_sitelib}/%{name}/vendor/click_completion/LICENSE
%license %{python3_sitelib}/%{name}/vendor/cursor/LICENSE
%license %{python3_sitelib}/%{name}/vendor/passa/LICENSE
%license %{python3_sitelib}/%{name}/vendor/pathlib2/LICENSE.rst
%license %{python3_sitelib}/%{name}/vendor/requirementslib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/resolvelib/LICENSE
%license %{python3_sitelib}/%{name}/vendor/scandir.LICENSE.txt
%license %{python3_sitelib}/%{name}/vendor/shutilwhich/LICENSE
%license %{python3_sitelib}/%{name}/vendor/tomlkit/LICENSE

%doc README.md NOTICES CHANGELOG.rst HISTORY.txt
%{_bindir}/pipenv
%{_bindir}/pipenv-resolver
%{python3_sitelib}/%{name}
%{python3_sitelib}/%{name}-%{version}-py%{python3_version}.egg-info

%files -n %{name}-doc
%doc html
%license LICENSE

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Oct 30 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-12
- Keep pathlib2, scandir, click-completion and backports.* bundled (#1767003)
- Keep tomlkit bundled for the same reason

* Fri Oct 11 2019 Patrik Kopkan <pkopkan@redhat.com> - 2018.11.26-11
- Devendored: yaspin vistir pythonfinder plette pipreqs pipdeptree pip_shims tomlkit

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-10
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Mon Aug 19 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-9
- Rebuilt for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Mar 13 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-7
- Require which (#1688145)

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2018.11.26-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jan 24 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-5
- Fix a fix of unbundling of packaging (sorry)

* Tue Jan 22 2019 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-4
- Fix unbundling of packaging
- Fixes https://github.com/pypa/pipenv/issues/3469

* Wed Jan  9 2019 Owen Taylor <otaylor@redhat.com> - 2018.11.26-3
- Fix pexpect import for compatibility mode of pipenv shell

* Wed Dec 19 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-2
- Use the system level root certificate instead of the one bundled in certifi

* Thu Nov 29 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.26-1
- Update to 2018.11.26 (bugfixes only)

* Fri Nov 23 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.11.14-1
- Update to 2018.11.14 (#1652091)
- Should fix incompatibility with pip (#1651317)

* Wed Aug 01 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-2
- Correct the name of bundled dotenv to python-dotenv

* Fri Jul 27 2018 Miro Hrončok <mhroncok@redhat.com> - 2018.7.1-1
- Update to 2018.7.1 (#1609432)

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 11.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 30 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-3
- Do not require pathlib2, it's intended for Python < 3.5

* Tue Jun 19 2018 Miro Hrončok <mhroncok@redhat.com> - 11.10.4-2
- Rebuilt for Python 3.7
- Add patch for patched/bundled prettytoml to work with 3.7

* Fri Apr 13 2018 Michal Cyprian <mcyprian@redhat.com> - 11.10.4-1
- Initial package.

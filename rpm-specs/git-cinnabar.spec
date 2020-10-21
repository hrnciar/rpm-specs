#global rcver b4
%global bundled_git_version 2.26.2
%global gitexecdir %{_libexecdir}/git-core
%global _python_bytecompile_extra 0

Name:           git-cinnabar
Version:        0.5.5
Release:        3%{?dist}
Summary:        Git remote helper to interact with mercurial repositories

License:        GPLv2
URL:            https://github.com/glandium/git-cinnabar
Source0:        https://github.com/glandium/%{name}/archive/%{version}%{?rcver}/%{name}-%{version}%{?rcver}.tar.gz
Source1:        https://mirrors.edge.kernel.org/pub/software/scm/git/git-%{bundled_git_version}.tar.xz
# Skip stuff that's not relevant for a tarball.
Patch0001:      0001-Skip-version-checks.patch
# hg clone https://hg.mozilla.org/users/mh_glandium.org/jqplot &&
# cd jqplot &&
# hg bundle --all ../jqplot$(hg id -i).hg
Source2:        jqplot-e8af8a37f0f1.hg
# Shebangs must match package requirements.
Patch0002:      0002-Make-Python-shebangs-explicit.patch

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  perl-macros
BuildRequires:  python2-devel
BuildRequires:  hg >= 1.9
# Bundled git requirements:
BuildRequires:  git
BuildRequires:  libcurl-devel
BuildRequires:  zlib-devel >= 1.2

Requires:       git-core
Requires:       hg >= 1.9

Provides:       bundled(git) = %{bundled_git_version}

%description
git-cinnabar is a git remote helper to interact with mercurial repositories.
Contrary to other such helpers, it doesn't use a local mercurial clone under
the hood, although it currently does require mercurial to be installed for some
of its libraries.


%prep
%autosetup -p1 -n %{name}-%{version}%{?rcver}
%setup -D -T -n %{name}-%{version}%{?rcver} -q -a 1
rmdir git-core
mv git-%{bundled_git_version} git-core

# Use these same options for every invocation of 'make'.
# Otherwise it will rebuild in %%install due to flags changes.
# Pipe to tee to aid confirmation/verification of settings.
cat << \EOF | tee config.mak
V = 1
CFLAGS = %{build_cflags}
LDFLAGS = %{build_ldflags}
NEEDS_CRYPTO_WITH_SSL = 1
USE_LIBPCRE = 1
ETC_GITCONFIG = %{_sysconfdir}/gitconfig
INSTALL_SYMLINKS = 1
GITWEB_PROJECTROOT = %{_localstatedir}/lib/git
GNU_ROFF = 1
NO_PERL_CPAN_FALLBACKS = 1
NO_PYTHON = 1
htmldir = %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
prefix = %{_prefix}
perllibdir = %{perl_vendorlib}
gitwebdir = %{_localstatedir}/www/git

# Test options
DEFAULT_TEST_TARGET = prove
GIT_PROVE_OPTS = --verbose --normalize %{?_smp_mflags} --formatter=TAP::Formatter::File
GIT_TEST_OPTS = -x --verbose-log
EOF


%build
%make_build helper


%install
# Can't make_install because it tries to build all of git.
install -d %{buildroot}%{gitexecdir}
install -p -m 0755 git-cinnabar %{buildroot}%{gitexecdir}
install -p -m 0755 git-cinnabar-helper %{buildroot}%{gitexecdir}
install -p -m 0755 git-remote-hg %{buildroot}%{gitexecdir}
install -d %{buildroot}%{gitexecdir}/cinnabar
install -p -m 0644 cinnabar/*.py %{buildroot}%{gitexecdir}/cinnabar
install -d %{buildroot}%{gitexecdir}/cinnabar/cmd
install -p -m 0644 cinnabar/cmd/*.py %{buildroot}%{gitexecdir}/cinnabar/cmd
install -d %{buildroot}%{gitexecdir}/cinnabar/hg
install -p -m 0644 cinnabar/hg/*.py %{buildroot}%{gitexecdir}/cinnabar/hg

%py_byte_compile %{__python2} %{buildroot}%{gitexecdir}/cinnabar


%check
# Check the installed copies.
mkdir gitexecdir
for f in %{gitexecdir}/* %{buildroot}%{gitexecdir}/*; do
    ln -s $f gitexecdir/
done
export GIT_EXEC_PATH=$PWD/gitexecdir
rm -r cinnabar
ln -s %{buildroot}%{gitexecdir}/cinnabar

%{__python2} -m unittest discover -v -s tests/ -p '*.py'
make -f CI/tests.mk REPO=%SOURCE2 check check-graft


%files
%doc README.md
%license COPYING
%{gitexecdir}/git-cinnabar
%{gitexecdir}/git-cinnabar-helper
%{gitexecdir}/git-remote-hg
%{gitexecdir}/cinnabar


%changelog
* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-3
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Fri Feb 14 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.4-1
- Update to latest version

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Nov 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.2-3
- Switch to unittest for running tests

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Jul 15 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.2-1
- Update to latest version

* Wed May 08 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.1-1
- Update to latest version

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-1
- Update to latest release

* Sat Aug 11 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-0.6.b4
- Update git config options to match plain git

* Mon Jul 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-0.5.b4
- Update to latest beta

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.5.0-0.4.b3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jun 16 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-0.3.b3
- Make Python byte-compilation explicit

* Sun May 20 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-0.2.b3
- Update to latest beta

* Tue Apr 10 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0.5.0-0.1.b2
- initial package for Fedora

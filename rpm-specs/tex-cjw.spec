%global texpkg    cjw
%global texpkgdir %{_texmf_main}/tex/latex/%{texpkg}
%global texpkgdoc %{_texmf_main}/doc/latex/%{texpkg}

Name:             tex-cjw
Version:          20090907
Release:          6%{?dist}
Summary:          LaTeX class for writing resumes and cover letters
BuildArch:        noarch

License:          LPPL
Source0:          http://tug.ctan.org/macros/latex2e/contrib/cjw.zip

BuildRequires:    /usr/bin/kpsewhich
Requires:         tex(latex)
Requires(post):   /usr/bin/texhash
Requires(postun): /usr/bin/texhash

%description
cjw is a LaTeX class for writing resumes.

%prep
%setup -q -n cjw

%build

%install
install -d -m 755 %{buildroot}%{texpkgdir}
install -p -m 644 *.{cls,sty} %{buildroot}%{texpkgdir}/

%files
%{texpkgdir}

%post
%texlive_post

%postun
%texlive_postun

%posttrans
%texlive_posttrans

%changelog
* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 20090907-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Jul 13 2020 W. Michael Petullo <mike@flyn.org> - 20090907-5
- Simplify package name to cjw
- Remove texmf definition from first line of specification

* Sun Jul 12 2020 W. Michael Petullo <mike@flyn.org> - 20090907-4
- Use global, not define
- Use predefined macros
- Run the TeX Live macros

* Sun Jul 12 2020 W. Michael Petullo <mike@flyn.org> - 20090907-3
- Remove use of defattr
- Remove rm -rf of buildroot
- Remove use of Group
- Update Source0

* Sun Feb 14 2010 W. Michael Petullo <mike@flyn.org> - 20090907-2
- Require tex(latex)
- Put braces around buildroot

* Sun Sep 07 2009 W. Michael Petullo <mike@flyn.org> - 20090907-1
- Initial package

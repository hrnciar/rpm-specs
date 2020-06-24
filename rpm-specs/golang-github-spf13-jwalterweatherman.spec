# Generated by go2rpm
%bcond_without check

# https://github.com/spf13/jwalterweatherman
%global goipath         github.com/spf13/jwalterweatherman
Version:                1.1.0

%gometa

# Remove in F33
%global godevelheader %{expand:
Obsoletes:      golang-github-spf13-jwalterweatherman-devel < 0-0.17
}

%global common_description %{expand:
Seamless printing to the terminal (stdout) and logging to a io.Writer (file)
that’s as easy to use as fmt.Println.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        5%{?dist}
Summary:        Seamless printing to the terminal and logging to a file

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%if %{with check}
# Tests
BuildRequires:  golang(github.com/stretchr/testify/require)
%endif

%description
%{common_description}

%gopkg

%prep
%goprep

%install
%gopkginstall

%if %{with check}
%check
%gocheck
%endif

%gopkgfiles

%changelog
* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Jul 09 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-3
- Add Obsoletes for old name

* Fri Apr 26 14:53:07 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 1.1.0-2
- Update to new macros

* Sun Mar 03 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Update to latest tagged version

* Tue Feb 05 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.0.0-1
- Update to first tagged version

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.20170523git0efa520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.15.20170523git0efa520
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.20170523git0efa520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Feb 27 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20170523git0efa520
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.git0efa520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.git0efa520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.git0efa520
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jun 10 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.9.git0efa520
- Bump to upstream 0efa5202c04663c757d84f90f5219c1250baf94f
  related: #1413107

* Wed Mar 01 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.8.git33c24e7
- Fix the import path prefix so it complies to its directory name under GOPATH
  resolves: #1427336

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.git33c24e7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Jan 14 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.6.git33c24e7
- Bump to upstream 33c24e77fb80341fe7130ee7c594256ff08ccc46
  related: #1413107

* Fri Jan 13 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.5.git3d60171
- Polish the spec file
  resolves: #1413107

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.git3d60171
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.3.git3d60171
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git3d60171
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct 08 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git3d60171
- First package for Fedora
  resolves: #1270061

%bcond_without check

# https://github.com/yuin/goldmark
%global goipath         github.com/yuin/goldmark
Version:                1.1.32

%gometa

%global common_description %{expand:
A markdown parser written in Go. Easy to extend, standard(CommonMark)
compliant, well structured.}

%global golicenses      LICENSE
%global godocs          README.md

Name:           %{goname}
Release:        1%{?dist}
Summary:        Markdown parser written in Go

License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

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
* Sat Jun 06 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.32-1
- Update to latest version

* Sun May 24 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.31-1
- Update to latest version

* Thu Apr 16 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.30-1
- Update to latest version

* Wed Apr 15 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.29-1
- Update to latest version

* Wed Apr 08 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.27-1
- Update to latest version

* Thu Mar 26 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.26-1
- Update to latest version

* Mon Mar 09 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.25-1
- Update to latest version

* Mon Mar 02 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.24-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.23-1
- Update to latest version

* Tue Feb 18 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.22-1
- Update to latest version

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Jan 01 2020 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.19-1
- Update to latest version

* Wed Oct 16 06:30:44 EDT 2019 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 1.1.0-1
- Initial package

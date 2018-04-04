Summary:	Python interface to systemd
Name:		python-systemd
Version:	234
Release:	1
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/systemd/python-systemd
Source0:	https://github.com/systemd/python-systemd/archive/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(libsystemd)

%description
Provides Python scripting interface to systemd.

%prep
%setup -q

%build
%setup_compile_flags
%{__python} setup.py build_ext -i

%install
%{__python} setup.py install --root=%{buildroot}

%files
%doc README.md LICENSE.txt NEWS
%{py_platsitedir}/systemd/test/*.py
%{py_platsitedir}/systemd/*.py
%{py_platsitedir}/systemd/*.so
%{py_platsitedir}/*.egg-info
%{py_platsitedir}/systemd/__pycache__/*.pyc
%{py_platsitedir}/systemd/test/__pycache__/*.pyc

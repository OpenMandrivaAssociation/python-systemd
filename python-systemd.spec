Summary:	Python interface to systemd
Name:		python-systemd
Version:	231
Release:	3
Group:		System/Kernel and hardware
License:	LGPLv2+
Url:		https://github.com/systemd/python-systemd
Source0:	https://github.com/systemd/python-systemd/archive/v%{version}.tar.gz
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
%{py_platsitedir}/python_systemd-%{version}-py%{py_ver}.egg-info
